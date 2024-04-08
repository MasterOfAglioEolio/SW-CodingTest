from collections import defaultdict

# 더블 링크드 리스트
# 구현

# 7
# 100 12 3 10 12 20 15 14 19 22 25 16 17 21 18 30 30 20 20 10 18 17 15 25 11 14 17
# 200 25
# 300 22
# 300 999
# 400 14
# 400 18
# 500 3


class Box:
    # 연결리스트 노드 생성자
    def __init__(self, box_id, weight):
        self.box_id=box_id
        self.weight=weight
        self.prev_box=None
        self.next_box=None

    # 노드의 앞과 뒤 주소를 넣어줌
    def set_prev(self, prev_box):
        self.prev_box=prev_box
    def set_next(self,next_box):
        self.next_box=next_box

    #앞의 노드와 연결 끊기
    def cut_prev(self):
        if self.prev_box==None:
            return
        self.prev_box.next_box=None
        self.prev_box=None

    #연결 리스트 중간에서 노드 제거
    def rid_box(self):
        if self.next_box:
            self.next_box.prev_box=self.prev_box
        if self.prev_box:
            self.prev_box.next_box=self.next_box

        self.prev_box=None
        self.next_box=None

class Belt:
    # 첫 상자와 끝상자 가리킬 변수
    # 상자 ID 검색을 위해 box_dict
    # 벨트 고장여부 저장 broken
    def __init__(self):
        self.first_box=None
        self.last_box=None
        self.box_dict={}
        self.broken=False

    # 벨트 끝에 상자 추가
    # 끝 상자와 추가할 상자 이어주기
    # 상자가 없을 때 호출되면 첫상자를 해당상자로 지정

    def add_box(self,this_box):
        self.box_dict[this_box.box_id]=this_box

        if not self.first_box:
            self.first_box=this_box

        if self.last_box:
            self.last_box.set_next(this_box)
            this_box.set_prev(self.last_box)

        self.last_box=this_box

    # 벨트 가장 앞 상자 unload 하기
    # 두번째 상자를 첫상자로 바꾸고, 앞상자와 연결 끊음
    # 상자가 1개이면 끝 상자도 None으로 바꿈

    def pop_box(self):

        box_to_pop=self.first_box
        self.first_box=box_to_pop.next_boxt

        if self.first_box:
            self.first_box.cut_prev()
        else:
            self.last_box=None

        del self.box_dict[box_to_pop.box_id]

        return box_to_pop

class Factory:


    # 1. 공장설립 = 100
    # 1-2) m개의 벨트를 설치하고, 각 벨트 위에 정확이 n/m개의 물건을 놓아 총 n개의 물건을 준비함
    #      ex) n = 12 m =3
    # 1-3) 각 물건에는 고유한 번호(ID)와 무게(W)가 적혀져 있음 (번호는 상자마다 다르지만, 무게가 동일함)
    def __init__(self,args):
        n,m,*presents=args
        counts=n//m
        self.belts=[Belt() for _ in range(m)]

        for idx,belt in enumerate(self.belts):
            for num in range(idx * counts, (idx+1)*counts):
                belt.add_box(Box(presents[num],presents[num+n]))

    # 2. 물건 하차 = 200
    # 2-2) 최대 무게 w_max가 주어짐
    # 2-3) 1번부터 m번까지 순서대로 벨트를 보며 각 벨트 맨 앞에 있는 선물 중 해당 선물의 무게가 w_max 이하라면 하차
    # 2-4) 그렇지 않다면 벨트 맨 뒤로 보냄
    # 2-5) 벨트에 있던 상자가 빠지면 한 칸씩 앞으로 내려와야 함
    # ex) w_max가 25라면 1번 상자 맨 뒤로, -> 2번 3번 상자 하차 -> 하차된 상자 무게 총합 2+3 (35) 출력

    def unload(self, max_wegiht):
        result=0

        for belt in self.belts:
            if belt.first_box:
                popped_box=belt.pop_box()
                if popped_box.weight<=max_wegiht:
                    result+=popped_box.weight
                else:
                    belt.add_box(popped_box)

    # 3. 물건 제거 = 300
    # 3-2) 제거하기 원하는 물건 r_id가 주어짐
    # 3-3) 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면, 해당 벨트에서 상자를 제거하고, 이에 따라 뒤에 있던 상자들 앞으로 한칸씩
    # ex) r_id 22 가 있다면 해당 상자 제거 / 없으면 -1 출력
    def remove(self, remove_id):
        result=-1

        for belt in self.belts:
            if remove_id in belt.box_dict:
                removed_box = belt.box_dict[remove_id]
                if belt.first_box == removed_box:
                    belt.first_box=removed_box.next_box
                if belt.last_box==removed_box:
                    belt.last_box=removed_box.prev_box

                removed_box.rid_box()
                result=removed_box.box_id
                del belt.box_dict[removed_box.box_id]
                break

        return result

    # 4. 물건 확인 = 400
    # 4-1) 산타가 확인하기를 원하느 물건의 고유번호 f_id 가 주어짐
    # 4-2) 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면 해당 벨트의 번호 출력 / 없으면 -1 출력
    # 4-3) 상자가 있는 경우 해당 상자 위에 있는 모든 상자를 전부 앞으로 가져옴 (가져올 시 순서는 그대로 유지)
    # ex) f_id 14면 없어서 -1 / f_id 18이면 벨트번호 3 출력 이후 18 앞에 있는 상자 모두 앞으로 당김
    def find(self, find_id):
        result =-1

        for belt_id, belt in enumerate(self.belts):
            if find_id in belt.box_dict:
                found_box=belt.box_dict[find_id]

            if belt.first_box != found_box:
                belt.first_box.set_prev(belt.last_box)
                belt.last_box.set_next(belt.first_box)
                belt.first_box=found_box
                belt.last_box=found_box.prev_box

                found_box.cut_prev()

            result=belt_id+1
            break

        return result

    # 5. 벨트 고장 = 500
    # 5-2) 고장이 발생한 b_num이 주어짐
    # 5-3) 해당 벨트는 다시 사용할 수 없게되고, b_num 벨트의 바로 오른쪽 벨트부터 순서대로 아직 고장나지 않은 최초 벨트 위로
    # 5-4) b_num 벨트에 놓여져있던 상자들을 아래부터 순서대로 하나씩 옮겨짐
    # 5-5) 만약 m번까지 봤는데 없다? -> 다시 1번부터 순서대로 벨트 확인
    #     (b_num번째 벨트를 제외한 벨트 중 최소 하나 이상이 정상 상태임을 가정해도 괜찮 / 즉 모든 벨트가 망가질 일은 없음)
    # ex) b_num =3 -> 3번 벨트가 망가짐 -> 이 명령 전 b_num 벨트가 이미 망가져있으면  -1 / 그렇지 않다면 b_num 출력
    def die(self, belt_id):
        result=-1
        belt_id=-1

        if self.belts[belt_id].broken == False:
            result=belt_id+1
            broken_belt=self.belts[belt_id]
            broken_belt.broken=True

            if len(broken_belt.box_dict):
                for idx in range(belt_id,belt_id+len(self.belts)):
                    if self.belts[idx%len(self.belts)].broken==False:
                        found_belt=self.belts[idx%len(self.belts)]

                        found_belt.box_dict.update(broken_belt.box_dict)
                        broken_belt.box_dict={}

                        found_belt.add_box(broken_belt.first_box)
                        found_belt.last_box=broken_belt.last_box
                        broken_belt.first_box=broken_belt.last_box=None
                        break

        return result



# 명령 입력
q=int(input())
#명령 초기화
order=[[] for _ in range(q)]

#명령 저장
for i in range(q):
    order[i]=list(map(int,input().split()))

print(order)

factory = Factory(order[0][1:])

for i in range(1,q):

    if order[i][0]==200:
        factory.unload(order[i][1])
    elif order[i][0]==300:
        factory.remove(order[i][1])
    elif order[i][0]==400:
        factory.find(order[i][1])
    elif order[i][0]==500:
        factory.die(order[i][1])

