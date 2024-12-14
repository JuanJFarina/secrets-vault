# secrets-vault
A secrets vault system inspired in Hashicorp Vault and used as example for my upcoming article on Domain-Driven Design. The system leverages a Ports and Adapters (a.k.a. Hexagonal, Onion, or Clean Architecture) together with an Event-Sourced Domain Model, and a Testing Pyramid emphasizing Unit Tests over Integration and E2E Tests (Shift-Left).

## Architecture

```mermaid
graph TD
    A[Secrets Vault System] -->|Domain| B[SecretsVault]
    B -->|Value Object| C[VaultPath]
    B -->|Value Object| D[Secret]

    A -->|Ports| E[API Interface]
    A -->|Adapters| F[File Adapter]
    A -->|Adapters| G[SQLAlchemy Adapter]

    E -->|Save/Load Secrets| B
    F -->|Save to Folder/Files| H[Filesystem]
    G -->|Persist Events| I[SQLite Database]

    subgraph Architecture
        A
        B
        C
        D
    end

    subgraph Infrastructure
        F
        G
        H
        I
    end
```

```mermaid
architecture-beta
    group secretsvault(server)[Secrets Vault System]
    group infralayer(server)[Infrastructure Layer] in secretsvault

    service infra(disk)[Infrastructure Layer] in infralayer
    service application(disk)[Application Layer] in infralayer
    service domain(disk)[Domain Layer] in infralayer

    application:R --> L:infra
    infra:R --> L:domain

    group applayer(server)[Application Layer] in secretsvault

    service infras(disk)[Infrastructure Layer] in applayer
    service app(disk)[Application Layer] in applayer
    service dom(disk)[Domain Layer] in applayer

    app:R --> L:infras
    infras:R --> L:dom

    domain:B --> T:app

    group domainlayer(server)[Domain Layer] in secretsvault

    service infrast(disk)[Infrastructure Layer] in domainlayer
    service appl(disk)[Application Layer] in domainlayer
    service doma(disk)[Domain Layer] in domainlayer

    appl:R --> L:infrast
    infrast:R --> L:doma

    dom:B --> T:appl
```
