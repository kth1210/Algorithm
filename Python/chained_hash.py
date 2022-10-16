from __future__ import annotations
from typing import Any, Type
import hashlib

#해시 구성하는 노드
class Node:
    #초기화
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


#체인법으로 해시 클래스 만들기
class ChainedHash:
    #초기화
    def __init__(self, capacity : int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    #해시값 구하기
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):        #key가 int형인 경우
            return key % self.capacity
        #key가 int형이 아닌 경우
        return (int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)

    #키가 key인 원소 검색하여 value 반환
    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)     #검색하는 키의 해시값
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value          #검색 성공
            p = p.next
        
        return None     #검색 실패

    #키가 key이고 값이 value인 원소 추가
    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)     #추가하는 키의 해시값
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False            #추가 실패
            p = p.next
        
        temp = Node(key, value, self.table[hash])   #추가할 노드 만들기
        self.table[hash] = temp         #노드 추가
        return True                     #추가 성공
    

    #키가 key인 원소 삭제
    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)     #삭제할 키의 해시값
        p = self.table[hash]
        pp = None                       #앞 노드를 위한 변수

        while p is not None:
            if p.key == key:
                if pp is None:          #첫번째 노드일때
                    self.table[hash] = p.next
                else:                   #첫번째 노드가 아닐때
                    pp.next = p.next
            return True                 #삭제 성공
            pp = p
            p = p.next
        
        return False                    #삭제 실패
    
    #원소를 출력
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')

            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()

    