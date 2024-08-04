import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cables)
    total_cost = 0
    
    # Об'єднуємо кабелі по два, поки не залишиться один
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Витрати на з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost
        
        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання:
cables = [19, 954, 18.9, 20]
print(f"Мінімальні загальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cables)}")
