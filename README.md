```markdown
# 🤖 DCIT Bot – Algerian Cyber Law Assistant

A Discord bot that answers questions about Algerian cyber law, digital citizenship, and IT offences. Built for ESI Alger's **Citoyenneté Numérique et IA** module. It uses a hybrid RAG pipeline (BM25 + embeddings + cross‑encoder) grounded in official legal texts.

---

## ✨ Features

### ⚖️ Cyber‑Law Assistant

- `/ask-law <question>` — Ask about Algerian cyber law (French or English)  
- `/law-help` — Show what the bot knows and how to use it  

The assistant never invents laws — it only answers from the provided PDFs. It cites articles and penalties directly from the texts.

---

## ⚖️ How the RAG Assistant Works

```text
knowledge_base/ (PDFs)
│
▼
ingest.py ──── pypdf (text extraction + boilerplate cleaning)
── article‑aware chunking
── paraphrase‑multilingual‑MiniLM‑L12‑v2 (embeddings)
── ChromaDB (vector DB with priority metadata)
── BM25 index (keyword search)
│
▼
rag_query.py ──── query expansion (Nmap → "394 bis accès frauduleux")
── cosine retrieval + BM25 retrieval
── Reciprocal Rank Fusion (RRF)
── forced TIC fetch for security queries
── cross‑encoder reranking (mmarco‑mMiniLMv2)
── priority boost (P1 docs)
── Groq API / Llama 3.3 70B
│
▼
bot/cogs/cyber_law_ai.py ──── /ask-law, /law-help
```

**Key design decisions:** - **Hybrid search** (cosine + BM25) ensures both semantic meaning and exact keywords (e.g., "394 bis") are used.  
- **Forced TIC fetch** for security‑related queries guarantees that the criminal law articles (394 bis–394 nonies) are always in the context.  
- **Cross‑encoder reranking** improves relevance over pure embedding similarity.  
- **Priority boost** gives core laws higher final scores.

---

## 📚 Knowledge Base

The bot relies on official Algerian legal texts. **PDFs are not included in this repository** – you must obtain them from official sources.

Required files (place in `knowledge_base/`):

| File | Description |
|------|-------------|
| `TIC_Articles.pdf` | Extracted from Code pénal (art. 394 bis–394 nonies) |
| `DZ_FR_Cybercrime Law_2009.pdf` | Loi 09‑04 (cybercrime) |
| `2018_Algeria_fr_Loi n_ 18-07...pdf` | Loi 18‑07 (data protection) |
| `Law 20-06 Algeria.pdf` | 2020 amendments |
| `Loi n∞ 15-04...pdf` | Electronic signature law |
| `Penal Procedure Code 2021 Update.pdf` | TIC court procedures |

> The full Penal Code (362 pages) can also be added, but the bot will prioritise `TIC_Articles.pdf` for security questions.

---

## 🚀 Setup

### 1. Clone and install dependencies

```bash
git clone [https://github.com/YoucefDjenfi/DCIT-Bot.git](https://github.com/YoucefDjenfi/DCIT-Bot.git)
cd DCIT-Bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your `DISCORD_TOKEN` and `GROQ_API_KEY` (get a free Groq API key at console.groq.com).

### 3. Add PDFs

Place the required PDFs (see table above) in the `knowledge_base/` folder.

### 4. Build the vector database and BM25 index

```bash
python3 ingest.py
```

This creates `chroma_db/` and `bm25_index.pkl`. Re‑run whenever you add or update PDFs.

### 5. Run the bot

```bash
python3 main.py
```

Slash commands will sync automatically on startup. The first run may take ~30‑60 seconds while models download.

---

## 💬 Commands

| Command | Description |
|---------|-------------|
| `/ask-law <question>` | Ask about Algerian cyber law (French or English) |
| `/law-help` | Information about the bot and its capabilities |

**Example queries:**
- `/ask-law Quelles sont les sanctions pour accès frauduleux à un système informatique ?`
- `/ask-law Est-il légal d'effectuer un scan Nmap sur un réseau Wi-Fi public ?`
- `/ask-law What are the penalties for unauthorized access to a computer system?`
- `/ask-law Que dit la loi 18-07 sur la collecte de données personnelles ?`

---

## 📁 Project Structure

```text
DCIT-Bot/
├── bot/
│   └── cogs/
│       └── cyber_law_ai.py          # Discord commands
├── knowledge_base/                  # PDFs (gitignored)
├── chroma_db/                       # auto‑generated vector DB (gitignored)
├── bm25_index.pkl                   # auto‑generated BM25 index (gitignored)
├── ingest.py                        # build the DB and index
├── rag_query.py                     # RAG pipeline (BM25, cosine, cross‑encoder)
├── document_priorities.py           # PDF priority mapping
├── config.py                        # environment variables
├── main.py                          # bot launcher
├── requirements.txt
└── .env.example
```

---

## ⚠️ Limitations & Disclaimer

- **Not a substitute for legal advice** – answers are AI‑generated and may contain errors. Always consult a qualified lawyer for real legal matters.
- **Hallucinations** – the LLM may occasionally invent article numbers or penalties. The system minimises this by forcing retrieved context, but it is not perfect.
- **French only** – the bot answers in French. English/Arabic queries are accepted but may be less accurate.
- **No continuous learning** – the bot does not learn from user interactions. Feedback is logged but not automatically applied.

---

## 🔮 Future Improvements (Planned)

- Fine‑tune the cross‑encoder on French legal question‑answer pairs.
- Add a `/law-feedback` command to collect user ratings.
- Implement confidence‑based fallback messages.
- Expand knowledge base with more Algerian decrees and international treaties.

---

## 🙏 Acknowledgements

- **Shellmates Club (ESI Alger)** – for the original bot structure that served as a learning playground.
- **Groq** – for free LLM inference (Llama 3.3 70B).
- **sentence-transformers** – for embeddings and cross‑encoder models.
- **Algerian government** – for publishing legal texts openly.

The original Shellmates fork is archived at github.com/YoucefDjenfi/DCIT-project for transparency.

---
Replace the old `README.md` in your `DCIT-Bot` repository with this cleaned version. Then commit and push:
```bash
git add README.md
git commit -m "docs: clean README, remove shellmates leftovers"
git push
```
