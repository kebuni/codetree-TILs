NO_BID = (0,0,0)
SCALE = 1000
N = SCALE*2+1
#grid = [[NO_BID for i in range(N)]for j in range(N)]
#next_grid = [[NO_BID for i in range(N)]for j in range(N)]
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
directs = {'U':0,'R':1,'D':2,'L':3}
last_collision = -1
bids_list = []
time = 0
############################

# def initialize_grid():
#     global grid
#     for i in range(N):
#         for j in range(N):
#             grid[i][j] = NO_BID

# def print_grid():
#     for i in range(N):
#         for j in range(N):
#             print(grid[i][j],end=' ')
#         print()

# def count_grid():
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if grid[i][j][0]:
#                 cnt += 1
#     return cnt

############################

TestCase = int(input())

for _ in range(TestCase):

    #initialize_grid()
    bids_list.clear()

    BidsNum = int(input())

    for bididx in range(BidsNum):
        x,y,w,d = input().split()
        x = int(x) * 2 + SCALE
        y = int(y) * -2 + SCALE
        #grid[y][x] = (int(w),int(bididx)+1,directs[d])
        bids_list.append((x,y,int(w),int(bididx)+1,directs[d]))

    #print_grid()
    time = 0   
    #print(bids_list) 
    
    for i in range(2*N):

        time += 1
        for bid in range(len(bids_list)):
            # 구슬을 옮긴다. in_range는 필요없다
            x,y,w,idx,d = bids_list[bid]
            bids_list[bid] = (x+dxs[d],y+dys[d],w,idx,d)
        
        #구슬을 다 옮겼으면 sort하고 중복 좌표 제거
        bids_list.sort()

        for bid in range(len(bids_list)-1):
            if bids_list[bid][0] == bids_list[bid+1][0] and \
                  bids_list[bid][1] == bids_list[bid+1][1]: #둘의 좌표가 같다면 앞에거 제거
                bids_list[bid] = (0,0,0,0,0)
                last_collision = time

        bids_list = list(filter(lambda x:x[2]!=0,bids_list))

        #print(bids_list) 
    
    print(last_collision)