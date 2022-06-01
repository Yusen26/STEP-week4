import numpy as np


def main():
  pages = {}

  with open('data/pages.txt', encoding='utf-8') as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[page[0]] = page[1]

    links_to = [0] * len(pages)
    links_from = [0] * len(pages)
  with open('data/links.txt', encoding='utf-8') as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      # links_to[i]にはiに向かっている（隣接）リンクの数を格納
      # links_from[i]にはiから直接だとれるリンクの数を格納
      links_to[int(link[1])] += 1
      links_from[int(link[0])] += 1
    
  return pages, links_to, links_from

if __name__ == '__main__':
    pages, links_to, links_from = main()
    popular_link = input("Output file for popular link:")
    # 10000個以上のリンクから直接たどれて、10000個以上のリンクにたどれるリンクを出力
    f = open(popular_link,'w',encoding='utf-8')
    for i in range(len(pages)):
        if links_to[i]>=500:
            if links_from[i]>=500:
                f.write(pages[str(i)] + " to it:" + str(links_to[i]) + " from it:" + str(links_from[i]) + "\n")
    f.close()
    
    isolated_link = input("Ourpur file for isolated link:")
    # 孤立したリンクを出力
    f = open(isolated_link,'w',encoding='utf-8')
    for i in range(len(pages)):
        if links_to[i]==0:
            if links_from[i]==0:
                f.write(pages[str(i)] + " " + str(links_to[i]) + " " + str(links_from[i]) + "\n")
    f.close()
    
    #最も多くのリンクからたどれるリンクを出力
    max_i = np.argmax(links_to)
    print(pages[str(max_i)], links_to[max_i])
    