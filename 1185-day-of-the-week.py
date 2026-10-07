class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        days = [31, 29 if (year%4==0 and year%100!=0) or year%400==0 else 28,
                31,30,31,30,31,31,30,31,30,31]
        count = sum(366 if i%4==0 else 365 for i in range(1971, year))
        count += sum(days[:month-1]) + day
        return week[(count + 4) % 7]
