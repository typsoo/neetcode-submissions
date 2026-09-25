from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        tcounts = Counter(t)
        scounts = defaultdict(int)

        required = len(tcounts)  # Сколько уникальных символов из t нужно покрыть
        matches = 0              # Сколько уникальных символов покрыто сейчас

        res_len = float("inf")
        res_l, res_r = -1, -1
        l = 0

        for r in range(len(s)):
            ch = s[r]
            scounts[ch] += 1

            # Фиксируем выполнение нормы для символа строго по равенству
            if ch in tcounts and scounts[ch] == tcounts[ch]:
                matches += 1

            # Окно валидно — сжимаем его слева до упора
            while matches == required:
                # Обновляем минимальное окно
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res_l, res_r = l, r

                # Выбрасываем левый символ
                left_ch = s[l]
                scounts[left_ch] -= 1
                
                # Если после удаления частота стала меньше требуемой — окно ломается
                if left_ch in tcounts and scounts[left_ch] < tcounts[left_ch]:
                    matches -= 1

                l += 1

        return "" if res_l == -1 else s[res_l : res_r + 1]