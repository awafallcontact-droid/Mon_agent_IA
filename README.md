# Agent IA Rodium

Assistant IA personnel avec une interface de chat web et une API Python. L’agent peut répondre aux messages et utiliser des outils pour effectuer des recherches sur le Web, consulter la météo, rechercher des pages Notion et envoyer des e-mails.

## Fonctionnalités

- Chat en français avec un agent propulsé par `openai/gpt-4o-mini` via la passerelle Rodium AI.
- Recherche sur le Web avec Tavily.
- Consultation de la météo avec WeatherAPI.
- Recherche dans un espace Notion.
- Envoi d’e-mails via Gmail.
- API HTTP construite avec FastAPI et interface web légère en HTML, CSS et JavaScript.

## Structure du projet

```text
.
├── index.html   # Interface de chat
├── main.py      # API FastAPI et configuration de l’agent
└── tools.py     # Outils de recherche, météo, Notion et e-mail
```

## Prérequis

- Python 3.10 ou une version ultérieure
- Des clés d’API pour les services que vous souhaitez utiliser

## Installation

1. Clonez le dépôt et placez-vous dans le dossier du projet :

   ```bash
   git clone https://github.com/awafallcontact-droid/Mon_agent_IA.git
   cd Mon_agent_IA
   ```

2. Créez et activez un environnement virtuel :

   ```bash
   python -m venv .venv
   ```

   Sous Windows (PowerShell) :

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   Sous macOS ou Linux :

   ```bash
   source .venv/bin/activate
   ```

3. Installez les dépendances :

   ```bash
   pip install fastapi "uvicorn[standard]" pydantic pydantic-ai python-dotenv requests tavily-python notion-client
   ```

## Configuration

Créez un fichier `.env` à la racine du projet et renseignez les clés nécessaires :

```env
OPENAI_API_KEY=votre_cle_rodium_ai
TAVILY_API_KEY=votre_cle_tavily
WEATHER_API_KEY=votre_cle_weatherapi
NOTION_API_KEY=votre_cle_notion
EMAIL_SENDER=votre_adresse_gmail
EMAIL_PASSWORD=votre_mot_de_passe_application_gmail
```

`OPENAI_API_KEY` est utilisé par le fournisseur OpenAI compatible de Rodium AI. L’adresse de la passerelle (`https://api.rodiumai.io/v1`) et le modèle sont configurés dans `main.py`.

Les clés des outils sont nécessaires uniquement pour les fonctionnalités correspondantes. Pour la recherche Notion, partagez les pages concernées avec votre intégration Notion. Pour Gmail, utilisez un mot de passe d’application plutôt que le mot de passe habituel du compte.

Ne publiez jamais votre fichier `.env` ni vos clés d’API.

## Lancement en local

1. Démarrez l’API :

   ```bash
   uvicorn main:app --reload
   ```

   L’API est alors disponible sur `http://127.0.0.1:8000`. La documentation interactive est accessible sur `http://127.0.0.1:8000/docs`.

2. Ouvrez `index.html` dans un navigateur pour utiliser l’interface. Par défaut, elle envoie ses requêtes à `http://127.0.0.1:8000/chat`.

## API

| Méthode | Route | Description |
| --- | --- | --- |
| `GET` | `/` | Vérifie que l’API est en ligne. |
| `POST` | `/chat` | Envoie un message à l’agent. |

Exemple de requête :

```json
{
  "message": "Quelle est la météo à Dakar ?"
}
```

La réponse contient le texte de l’agent dans le champ `reponse`.

## Déploiement

Aucun lien de déploiement public n’est actuellement configuré dans le projet. L’interface et l’API doivent être déployées séparément ou rendues accessibles via des URL publiques. Après le déploiement de l’API, remplacez dans `index.html` l’URL locale `http://127.0.0.1:8000/chat` par l’URL publique de la route `/chat`.

## Sécurité

L’API configure actuellement CORS pour autoriser toutes les origines. En production, limitez `allow_origins` aux domaines hébergeant votre interface.
