import os, sys, uuid
from datetime import datetime, timedelta
sys.path.insert(0, os.path.dirname(__file__))
os.environ['DATABASE_URL'] = ''

from main import SessionLocal, Order, ChatSession, ChatMessage, SupportTicket

def seed():
    db = SessionLocal()

    # --- Seed orders ---
    if db.query(Order).count() == 0:
        orders = [
            Order(order_id="A1B2C3D4", created_at=datetime.now()-timedelta(minutes=30),
                  amount_usdt=50.0, amount_rub=3782.0, rate_at_creation=75.64,
                  commission_percent=3.0, commission_amount=1.5,
                  currency="RUB", bank="Сбербанк", phone="+7 999 123 45 67",
                  deposit_address="TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
                  status="pending", order_type="buy", asset_type="USDT",
                  wallet="9x4K8J3p2QmR7vW1nL5tY6cB0fA2dE3gH6i"),
            Order(order_id="E5F6G7H8", created_at=datetime.now()-timedelta(hours=2),
                  amount_usdt=120.0, amount_rub=9076.8, rate_at_creation=75.64,
                  commission_percent=3.0, commission_amount=3.6,
                  currency="RUB", bank="Тинькофф", phone="+7 916 555 77 88",
                  deposit_address="SOL4K8J3p2QmR7vW1nL5tY6cB0fA2dE3gH6i",
                  status="paid", order_type="buy", asset_type="SOL",
                  wallet="5tY6cB0fA2dE3gH6i9x4K8J3p2QmR7vW1nL"),
            Order(order_id="J9K0L1M2", created_at=datetime.now()-timedelta(days=1),
                  amount_usdt=250.0, amount_rub=18910.0, rate_at_creation=75.64,
                  commission_percent=3.0, commission_amount=7.5,
                  currency="RUB", bank="Сбербанк", phone="+7 903 222 33 44",
                  deposit_address="0x4K8J3p2QmR7vW1nL5tY6cB0fA2dE3gH6i",
                  status="cancelled", order_type="buy", asset_type="ETH",
                  wallet="0x9x4K8J3p2QmR7vW1nL5tY6cB0fA2dE3gH6i"),
            Order(order_id="N3O4P5Q6", created_at=datetime.now()-timedelta(hours=12),
                  amount_usdt=100.0, amount_rub=7564.0, rate_at_creation=75.64,
                  commission_percent=3.0, commission_amount=3.0,
                  currency="RUB", bank="Альфа-Банк", phone="+7 985 444 55 66",
                  deposit_address="TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
                  status="paid", order_type="sell", asset_type="USDT",
                  wallet="F8dE3gH6i9x4K8J3p2QmR7vW1nL5tY6cB0"),
        ]
        for o in orders:
            db.add(o)
        db.commit()
        print(f"Seeded {len(orders)} orders")

    # --- Seed chat sessions ---
    if db.query(ChatSession).count() == 0:
        sessions = [
            ChatSession(id=1, created_at=datetime.now()-timedelta(hours=3),
                        status="active", unread=2,
                        ip_address="195.123.222.134", country_code="RU", country_name="Russia",
                        wallet="9x4K8J3p2QmR7vW1nL5tY6cB0fA2dE3gH6i"),
            ChatSession(id=2, created_at=datetime.now()-timedelta(days=1),
                        status="closed", unread=0,
                        ip_address="85.26.183.45", country_code="RU", country_name="Russia",
                        wallet="5tY6cB0fA2dE3gH6i9x4K8J3p2QmR7vW1nL"),
        ]
        for s in sessions:
            db.add(s)
        db.commit()
        print(f"Seeded {len(sessions)} chat sessions")

    # --- Seed chat messages ---
    if db.query(ChatMessage).count() == 0:
        messages = [
            ChatMessage(session_id=1, sender="client", message="Здравствуйте! Отправил 50 USDT, статус не меняется уже 15 минут",
                        created_at=datetime.now()-timedelta(hours=3)),
            ChatMessage(session_id=1, sender="admin", message="Здравствуйте! Проверяю ваш платёж. Подождите несколько минут, транзакция обрабатывается",
                        created_at=datetime.now()-timedelta(hours=2, minutes=55)),
            ChatMessage(session_id=1, sender="client", message="Спасибо, всё пришло! Заказ выполнен",
                        created_at=datetime.now()-timedelta(hours=2, minutes=30)),
            ChatMessage(session_id=2, sender="client", message="Добрый день! Какие лимиты на одну операцию?",
                        created_at=datetime.now()-timedelta(days=1)),
            ChatMessage(session_id=2, sender="admin", message="Добрый день! Минимальная сумма 10 USDT, максимальная 5000 USDT",
                        created_at=datetime.now()-timedelta(days=1, minutes=-45)),
            ChatMessage(session_id=2, sender="client", message="Понял, спасибо!",
                        created_at=datetime.now()-timedelta(days=1, minutes=-40)),
        ]
        for m in messages:
            db.add(m)
        db.commit()
        print(f"Seeded {len(messages)} chat messages")

    db.close()

if __name__ == "__main__":
    seed()
    print("Done")
