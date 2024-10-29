# Interview Task: Implementing a “Post” Model with FastAPI

Imagine you’re building a backend for a social media platform similar to X/Twitter.
Users can create short posts (like tweets), which we’ll refer to as "posts". Each post belongs to a user and contains a title and content.

## Provided Model Definition

Below is a basic Post model. Your task is to implement the database schema, API endpoints, and tests to support creating, retrieving, and deleting posts.

```python
class Post(Base):
    __tablename__ = "post"
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="posts", lazy="select")

```

## How to get started

```bash
python3.12 -m venv env
source env/bin/activate
```

Run the following command to install dependencies.

```bash
pip install -r requirements.txt
```

## Run the app locally

```bash
python run.py
```

## API docs

http://localhost:8000/docs

## Run tests

We use the `TestConfig` to run tests

```bash
bash test.sh
```

