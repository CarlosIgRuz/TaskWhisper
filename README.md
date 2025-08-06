# TaskWhisper 🗣️🚀

*Voice-first task orchestrator that turns everyday conversations into actionable to-dos for crews & staff.*

<div align="center">
  <img src="docs/diagram.png" width="60%" alt="high-level architecture diagram"/>
</div>

## ✨ ¿Qué es?

TaskWhisper escucha diálogos (por ejemplo, camarero–cliente o jefe de obra–equipo),  
transcribe el audio con **Whisper**, detecta la **intención** con un LLM y dispara la acción correcta
(enviar orden a cocina, crear reserva, asignar check-list, etc.).  
Todo en tiempo real y sin manos.

## 🍱 Tech-stack

| Capa | Tech |
|------|------|
| STT | OpenAI Whisper v3 (o Deepgram) |
| NLU | GPT-4o function-calling |
| Orquestación | LangChain + FastAPI |
| Mobile | React-Native (expo) |
| Infra | Docker Compose + PostgreSQL |

## 🚀 Quick start

```bash
git clone https://github.com/tu-user/taskwhisper.git
cd taskwhisper
docker compose up --build
