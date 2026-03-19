# Stack de Monitoring — Prometheus + Grafana + Alertmanager

Stack de monitoring conteneurisé déployé sur VM Ubuntu Server via Docker Compose.

## Architecture
```
Node Exporter (9100) → Prometheus (9090) → Alertmanager (9093)
                              │
                           Grafana (3000)
```

## Services

| Service | Rôle | Port |
|---|---|---|
| Prometheus | Collecte et stockage des métriques | 9090 |
| Node Exporter | Exposition des métriques système Linux | 9100 |
| Grafana | Visualisation des métriques | 3000 |
| Alertmanager | Gestion et envoi des alertes | 9093 |
| Webhook Logger | Réception des alertes (lab) | 5001 |

## Règles d'alerte configurées

- `HighCPUUsage` — CPU > 80% pendant 1 minute
- `HighMemoryUsage` — RAM > 80% pendant 1 minute
- `DiskSpaceLow` — Disque > 85% pendant 1 minute
- `InstanceDown` — Instance inaccessible depuis 30 secondes

## Lancer le stack
```bash
git clone https://github.com/<ton-username>/monitoring-lab.git
cd monitoring-lab
docker compose up -d
```

## Accès

| Interface | URL |
|---|---|
| Grafana | http://localhost:3000 |
| Prometheus | http://localhost:9090 |
| Alertmanager | http://localhost:9093 |

Identifiants Grafana par défaut : `admin` / `admin123`

## Technologies

Docker · Docker Compose · Prometheus · Grafana · Alertmanager · Node Exporter · PromQL · Linux · YAML
