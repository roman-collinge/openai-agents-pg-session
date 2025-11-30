# OpenAI Agents PostgreSQL Session

🛠️ Under development.

`openai-agents-pg-session` is a Python library that provides a PostgreSQL-Backed Session implementation for the OpenAI Agents SDK

## Installation

(You will be able to) Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `openai-agents-pg-session`.

```bash
pip install openai-agents-pg-session
```

## (Planned) Usage

```python
import openai-agents-pg-session

database_url = "postgresql://USER:PASSWORD@HOST:PORT/DATABASE"
session_id = "abc_123"

session = PostgresSession(session_id, database_url)

result = await Runner.run(
    agent,
    "Hello",
    session=session
)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
