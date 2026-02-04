// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

using EmptyAgent;
using Microsoft.Agents.Builder;
using Microsoft.Agents.Builder.App;
using Microsoft.Agents.Hosting.AspNetCore;
using Microsoft.Agents.Hosting.BotCore;
using Microsoft.Agents.Storage;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Teams.Bot.Core;
using Microsoft.Teams.Bot.Core.Hosting;

WebApplicationBuilder builder = WebApplication.CreateBuilder(args);

// Register IStorage for state management.
// For development, MemoryStorage is suitable.
// For production, use persisted storage (CosmosDB, Blob Storage, etc.)
builder.Services.AddSingleton<IStorage, MemoryStorage>();

// Register AgentApplicationOptions
builder.Services.AddSingleton(sp => new AgentApplicationOptions(sp.GetRequiredService<IStorage>()));

// Register Agent with BotCore compatibility layer
// This sets up BotApplication, CompatChannelAdapter, CompatAgentAdapter, and the Agent
builder.AddAgentWithBotCore<MyAgent>();

WebApplication app = builder.Build();


app.MapGet("/", () => "Microsoft Agents SDK Sample");

// This receives incoming messages from Azure Bot Service or other SDK Agents
var incomingRoute = app.MapPost("/api/messages", async (
    HttpRequest request,
    HttpResponse response,
    IAgentHttpAdapter adapter,
    IAgent agent,
    CancellationToken cancellationToken) =>
{
    await adapter.ProcessAsync(request, response, agent, cancellationToken);
});

if (!app.Environment.IsDevelopment())
{
    incomingRoute.RequireAuthorization();
}
else
{
    // Hardcoded for brevity and ease of testing.
    // In production, this should be set in configuration.
    app.Urls.Add("http://localhost:3978");
}

app.Run();
