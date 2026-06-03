**Логическая модель базы данных**

Таблица 1 – users
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| FullName | varchar(100) | ФИО пользователя |
| Email | varchar(100) | Электронная почта |
| Phone | varchar(16) | Номер телефона |
| PasswordHash | varchar(255) | Хэш пароля |
| RoleId | int | FK |
| IsDelete | smallint | Флаг мягкого удаления |
| CreatedAt | datetime | Дата регистрации |

Таблица 2 – roles
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| Name | varchar(50) | Название роли |
| IsDelete | smallint | Флаг мягкого удаления |

Таблица 3 – assets
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| Name | varchar(50) | Название актива (USDT, SOL) |
| Code | varchar(10) | Символьный код |
| Network | varchar(50) | Блокчейн-сеть (TRC20, Solana) |
| IsActive | tinyint(1) | Активен ли актив для обмена |
| IsDelete | smallint | Флаг мягкого удаления |

Таблица 4 – currencies
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| Code | varchar(10) | Код валюты (RUB, USD, EUR) |
| Name | varchar(100) | Название валюты |
| Symbol | varchar(10) | Символ валюты |
| IsDelete | smallint | Флаг мягкого удаления |

Таблица 5 – banks
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| CurrencyId | int | FK |
| Name | varchar(100) | Название банка |
| IsDelete | smallint | Флаг мягкого удаления |

Таблица 6 – orders
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| OrderId | varchar(50) | Публичный ID заказа |
| AssetId | int | FK |
| CurrencyId | int | FK |
| BankId | int | FK |
| AmountAsset | decimal(18,8) | Сумма криптовалюты |
| AmountFiat | decimal(18,2) | Сумма в фиатной валюте |
| Rate | decimal(18,2) | Курс на момент создания |
| CommissionPercent | decimal(5,2) | Процент комиссии |
| CommissionAmount | decimal(18,2) | Сумма комиссии |
| DepositAddress | varchar(255) | Адрес для оплаты |
| Status | varchar(50) | Статус заказа |
| BuyerPhone | varchar(16) | Телефон покупателя |
| CreatedAt | datetime | Дата создания |
| PaidAt | datetime | Дата оплаты |
| IsDelete | smallint | Флаг мягкого удаления |

Таблица 7 – order_statuses
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| OrderId | int | FK |
| Status | varchar(50) | Статус |
| ChangedAt | datetime | Дата изменения |
| ChangedBy | int | FK (userId) |

Таблица 8 – transactions
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| OrderId | int | FK |
| Signature | varchar(255) | Подпись транзакции в блокчейне |
| FromAddress | varchar(255) | Адрес отправителя |
| ToAddress | varchar(255) | Адрес получателя |
| Amount | decimal(18,8) | Сумма транзакции |
| AssetCode | varchar(10) | Код актива |
| Status | varchar(50) | Статус подтверждения |
| ConfirmedAt | datetime | Дата подтверждения |
| CreatedAt | datetime | Дата создания |
| IsDelete | smallint | Флаг мягкого удаления |

Таблица 9 – chat_sessions
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| ClientName | varchar(100) | Имя клиента |
| Email | varchar(100) | Email клиента |
| Status | varchar(50) | Статус сессии |
| Unread | int | Количество непрочитанных |
| CreatedAt | datetime | Дата создания |

Таблица 10 – chat_messages
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| SessionId | int | FK |
| Sender | varchar(20) | Отправитель (client/admin) |
| Message | text | Текст сообщения |
| CreatedAt | datetime | Дата и время отправки |

Таблица 11 – support_tickets
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| DepositAddress | varchar(255) | Адрес кошелька |
| OrderId | varchar(50) | ID заказа |
| Email | varchar(100) | Email |
| Message | text | Сообщение |
| Status | varchar(50) | Статус |
| CreatedAt | datetime | Дата создания |

Таблица 12 – rate_history
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| AssetCode | varchar(10) | Код актива |
| CurrencyCode | varchar(10) | Код валюты |
| BuyRate | decimal(18,2) | Курс покупки |
| CreatedAt | datetime | Дата фиксации курса |

Таблица 13 – wallet_addresses
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| AssetCode | varchar(10) | Код актива |
| Address | varchar(255) | Криптовалютный адрес |
| PrivateKey | varchar(255) | Приватный ключ (зашифрован) |
| Balance | decimal(18,8) | Текущий баланс |
| IsActive | tinyint(1) | Активен ли адрес |
| CreatedAt | datetime | Дата создания |

Таблица 14 – commission_settings
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| AssetCode | varchar(10) | Код актива |
| CommissionPercent | decimal(5,2) | Процент комиссии |
| IsActive | tinyint(1) | Активно ли правило |
| UpdatedAt | datetime | Дата обновления |

Таблица 15 – audit_log
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| UserId | int | FK |
| Action | varchar(100) | Действие |
| EntityType | varchar(50) | Тип сущности |
| EntityId | int | ID сущности |
| Details | text | Детали |
| IpAddress | varchar(50) | IP-адрес |
| CreatedAt | datetime | Дата действия |

Таблица 16 – payment_methods
| Название | Тип данных | Описание |
|----------|-----------|----------|
| Id | int | PK |
| Name | varchar(50) | Название (Наличные, Карта, Перевод) |
| CurrencyId | int | FK |
| IsActive | tinyint(1) | Активен ли метод |
| IsDelete | smallint | Флаг мягкого удаления |
