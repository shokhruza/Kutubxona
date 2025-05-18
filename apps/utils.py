from datetime import date

def calculate_penalty(order):
    today = date.today()
    if today > order.due_date:
        overdue_days = (today - order.due_date).days
        penalty = int(order.book.daily_price * 0.01 * overdue_days)
        return penalty
    return 0
