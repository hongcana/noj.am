n = int(input())
count = 0
li = list()

for _ in range(n):
    m_age, m_name = map(str, input().split())
    m_age = int(m_age)
    li.append((m_age, m_name))

li.sort(key = lambda age: (age[0]))

for mem in li:
    print(mem[0], mem[1])