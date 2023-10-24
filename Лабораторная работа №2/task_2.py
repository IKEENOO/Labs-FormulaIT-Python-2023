salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Подушка безопасности

while months:
    months -= 1
    if months == 9:
        money_capital = spend - salary
    else:
        spend += spend * increase
        money_capital += spend - salary

months = 10
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
