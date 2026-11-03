# promptLLM

## simpleprompt.py avec Ollama

`simpleprompt.py` envoie un prompt à un modèle qui tourne en local avec [Ollama](https://ollama.com) et affiche la réponse dans le terminal. C'est gratuit, aucune clé API n'est nécessaire, et rien ne sort de votre machine.

Le script passe par `ChatOpenAI` (LangChain), car Ollama accepte le même format d'API qu'OpenAI.

### Prérequis

Il faut installer deux outils : [uv](https://docs.astral.sh/uv/) et [Ollama](https://ollama.com).

**macOS**
```bash
brew install uv ollama
```

**Linux**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows** (dans PowerShell)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
winget install Ollama.Ollama
```
Si `winget` n'est pas disponible, téléchargez l'installateur d'Ollama sur [ollama.com/download](https://ollama.com/download).

Après l'installation, fermez puis rouvrez le terminal pour que les commandes `uv` et `ollama` soient reconnues.

Les commandes des sections suivantes sont identiques sur les trois systèmes.

### Installation

1. Télécharger un modèle (à faire une seule fois) :
   ```bash
   ollama pull gemma4:e4b
   ```
2. Installer les dépendances Python du projet :
   ```bash
   uv sync --extra openai
   ```
   `--extra openai` est nécessaire : `langchain-openai` fait partie des dépendances optionnelles. Un `uv sync` sans cette option le désinstalle.

### Utilisation

1. Vérifier que le serveur Ollama tourne :
   - **macOS et Windows** : ouvrir l'application Ollama. Elle reste ensuite active en arrière-plan, son icône est visible dans la barre des menus ou dans la zone de notification.
   - **Linux** : le script d'installation lance Ollama comme service, il démarre donc tout seul. Sinon, lancer `ollama serve` dans un terminal séparé.

   Pour tester, `ollama list` doit répondre sans erreur.
2. Lancer le script :
   ```bash
   uv run simpleprompt.py
   ```

### Changer le prompt ou le modèle

Pour l'instant, les deux se modifient directement dans `simpleprompt.py` :

- **Prompt** : la variable `prompt` en haut du fichier.
- **Modèle** : le paramètre `model=` de `ChatOpenAI`. Il doit correspondre à un modèle installé.

Pour voir les modèles installés :
```bash
ollama list
```

Modèles conseillés :

| Modèle | Usage |
|---|---|
| `gemma4:e4b` | Usage courant : rapide, et comprend les images |
| `gpt-oss:20b` | Code et questions difficiles. Plus lent, environ 13 Go de mémoire |

### Problèmes fréquents

| Erreur | Cause | Solution |
|---|---|---|
| `Connection refused` | Le serveur Ollama n'est pas lancé | Ouvrir l'application Ollama, ou lancer `ollama serve` |
| `uv` ou `ollama` : commande introuvable | Le terminal a été ouvert avant l'installation | Fermer puis rouvrir le terminal |
| `model "..." not found` | Le modèle n'est pas téléchargé | `ollama pull <modèle>` |
| `ModuleNotFoundError: No module named 'langchain_openai'` | Dépendance optionnelle non installée | `uv sync --extra openai` |
