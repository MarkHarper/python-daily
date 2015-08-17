#HackerRank submission for Project Euler Task 1, passed all test cases

inp = int(input())
for i in range(0, inp):
    n = int(input())
    m_three = (n-1) // 3
    m_five = (n-1) // 5
    m_teen = (n-1) // 15
    three = 3 * (m_three) * ((m_three)+1) // 2
    five = 5 * (m_five) * ((m_five)+1) // 2
    teen = 15 * (m_teen) * ((m_teen)+1) // 2
    a = (three) + (five) - (teen)
    print(str(a))
