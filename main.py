import matplotlib.pyplot as plt
import random
import math


def eu_dist(a: tuple, b: tuple):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


it = int(input('How many Times? '))
beta = float(input('Beta: '))
if beta > 1 or beta < 0:
    print('Error. Rewrite beta.')
    beta = float(input('Beta: '))
gamma = 1 / math.sqrt(1-beta**2)

ujeu_point_list = [(0, 0)]
ujeu_time = 0
for i in range(it):
    p_i = (random.random(), random.random())
    ujeu_point_list.append(p_i)
    ujeu_time += eu_dist(ujeu_point_list[i], ujeu_point_list[i-1])
ujeu_point_list.append((0, 0))
ujeu_time += eu_dist(ujeu_point_list[it], (0, 0))
print(ujeu_time)

# S'에서 빛의 경로
plt.figure(figsize=(5, 5))
for i in range(it+1):
    plt.plot(
        [ujeu_point_list[i][0], ujeu_point_list[i+1][0]], [ujeu_point_list[i][1], ujeu_point_list[i+1][1]], c='black'
    )
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.box(True)
plt.text(0, 1.05, f'Time: {ujeu_time}')
plt.savefig('ujeu.png')
plt.show()

# S에서의 빛의 경로
out_point_list = [(0, 0)]
out_time = 0
for i in range(1, it+2):
    delta_x = ujeu_point_list[i][0]-ujeu_point_list[i-1][0]
    delta_y = ujeu_point_list[i][1]-ujeu_point_list[i-1][1]
    out_point_list.append(
        (out_point_list[i-1][0] + (delta_x + beta * math.sqrt(delta_x**2 + delta_y**2)) / math.sqrt(1 - beta**2), ujeu_point_list[i][1])
    )
    out_time += eu_dist(out_point_list[i], out_point_list[i-1])
print(out_time)

plt.figure(figsize=(5 * out_point_list[it+1][0], 5))
for i in range(it+1):
    plt.plot(
        [out_point_list[i][0], out_point_list[i+1][0]], [out_point_list[i][1], out_point_list[i+1][1]], c='black'
    )
plt.xlim(0, out_point_list[it+1][0])
plt.ylim(0, 1)
plt.box(True)
plt.text(0, 1.05, f'Time: {out_time}')
plt.savefig('out.png')
plt.show()

print(out_time / ujeu_time, gamma)
