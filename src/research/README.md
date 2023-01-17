# Результаты сравнения Clickhouse и Vertica

Тест(запрос) | Vertica, с          | Clickhouse, с
---- |---------------------| ----------
Вставка 10 млн записей | 5559.677659034729   | 149.37802147865295
Количество всех записей | 0.13719677925109863 | 0.0037767887115478516
Количество уникальных пользователей | 0.17499184608459473 | 0.05501747131347656
Количество уникальных фильмов | 0.3166637420654297  | 0.07767033576965332
Количество уникальных фильмов по пользователям | 0.15091466903686523 | 0.2677769660949707
Просмотренное время по фильмам и пользователям | 0.8283319473266602  | 0.5848631858825684
Выборка по времени | 0.23641180992126465 | 0.09400439262390137

### Решение
Так как по всем выполненным тестам Clickhouse оказался быстрее Vertica, то принято решение использовать Clickhouse в качестве хранилища для сбора аналитической информации.