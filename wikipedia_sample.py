from collections import deque
import datetime

# 深さ優先探索
def dfs(start, target, links):
  # stackを用意
  container = deque()
  container.append(start)
  # stackはpopすると記録が残らない
  # stackに要素を積んだ順番にappend_orderに格納する
  append_order = []
  append_order.append(start)
  # n回目にpopした要素のappend_orderにおけるindexをbeforeにし
  # n+1回目にpopした要素のappend_orderにおけるindexをafterにする
  # stack新しく積まれた要素をpopするなら、after>beforeになり
  # 限界まで探索してもとに戻ってpopする場合は、after<beforeになる
  before = 0
  # stackに積んだらvisitedに入れる
  visited = []
  visited.append(start)
  # routeに経路を保存する
  route = []
  
  while container:
    
    v = container.pop()
    after = append_order.index(v)
    route.append(v)
    #print("route",route)
    
    # 先にstackに積まれたのに、その後に積まれた要素より遅くpopされる＝戻ってきたということ
    # 戻った部分はrouteから除外する
    if after<before:
      for i in append_order[after+1:before+1]:
        if i in route:
          route.remove(i)
    before = after
    
    if v == target:
      return route
    
    # vがtargetじゃない場合は、そのfollowをみる
    # visitedに入っていなければ、stackに積んで、visitedにし、append_orderにも追加しておく
    if v in links:
      v_follows = list(links[v])
      for follow in v_follows:
        if follow not in visited:
            container.append(follow)
            visited.append(follow)
            append_order.append(follow)
        if follow==target:
          break
            
      #print("order",append_order)
  return 'Not Found'

# dfsとほとんど同じ(popをpopleftに変更するだけ)
def bfs(start, target, links):
  container = deque()
  container.append(start)
  append_order = []
  append_order.append(start)
  before = 0
  visited = []
  visited.append(start)
  route = []
  
  while container:
    #print(container)
    v = container.popleft()

    after = append_order.index(v)
    route.append(v)
    #print("route",route)
    if after<before:
      for i in append_order[after+1:before+1]:
        if i in route:
          route.remove(i)
    before = after
    
    if v == target:
      return route
    
    if v in links:
      v_follows = list(links[v])
      for follow in v_follows:
        if follow not in visited:
          container.append(follow)
          visited.append(follow)
          append_order.append(follow)
      #print("order",append_order)
  return 'Not Found'


def main():
  pages = {}
  links = {}

  with open('data/pages.txt', encoding='utf-8') as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[page[0]] = page[1]

  with open('data/links.txt', encoding='utf-8') as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      if link[0] in links:
        links[link[0]].add(link[1])
      else:
        links[link[0]] = {link[1]}
    #print(links)
  
  return pages, links

if __name__ == '__main__':

  print("start reading", datetime.datetime.now())
    
  pages, links = main()

  print("finish reading", datetime.datetime.now())
    
  while True:
    start_page = input("Start:")
    target_page = input("Target:")
    searching_method = input("Searching Method:(dfs or bfs)")
    if searching_method!="dfs" and searching_method!="bfs":
      print('Searching Method should be either dfs or bfs')
      continue
    
    # startとtargetを飛ばすと終了
    if start_page=="" and target_page=="":
      break
    for k, v in pages.items():
      if v == start_page:
        print(v, k)
        start_id = k
      if v == target_page:
        print(v, k)
        target_id = k
    if searching_method=="dfs":
      route = dfs(start_id, target_id, links)
    else:
      route = bfs(start_id, target_id, links)
      
    print(route)
    print("finish searching", datetime.datetime.now())
