import heapq

def min_cost_to_connect_cables(cables):
    """
    Обчислює мінімальну вартість з'єднання всіх мережевих кабелів.
    
    Використовує модуль heapq для реалізації мінімальної купи (priority queue).
    Алгоритм жадібний: щоразу з'єднує два найкоротші кабелі.
    
    Args:
        cables (list[int]): Список довжин кабелів.
    
    Returns:
        int: Мінімальна загальна вартість з'єднань.
    """
    if len(cables) <= 1:
        return 0
    
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Витягуємо два найменші
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Вартість з'єднання - сума довжин
        connection_cost = first + second
        total_cost += connection_cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, connection_cost)
    
    return total_cost

# Приклад використання та тестування
if __name__ == "__main__":
    # Тестові дані
    cables1 = [4, 3, 2, 6]
    print(f"Кабелі: {cables1}")
    print(f"Мінімальна вартість: {min_cost_to_connect_cables(cables1)}")  # 29
    
    cables2 = [5, 4, 2, 8]
    print(f"Кабелі: {cables2}")
    print(f"Мінімальна вартість: {min_cost_to_connect_cables(cables2)}")  # 36
    
    cables3 = [1, 2]
    print(f"Кабелі: {cables3}")
    print(f"Мінімальна вартість: {min_cost_to_connect_cables(cables3)}")  # 3