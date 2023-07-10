def solution(cacheSize, cities):
    cache = []
    time = 0
    
    for city in cities:
        city = city.lower()
        # cache hit인 경우
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
            continue
            
        # cache miss인데 이미 버퍼가 가득 찼을 때
        if len(cache) >= cacheSize:
        
            # 캐시 크기가 0이라 못 들어가는 경우
            if cacheSize == 0:
                time += 5
                continue
                
            # 그 외
            else:
                cache.pop(0)
                time += 5
                cache.append(city)
                continue
        
        # cache miss인데 아직 새로 페이지를 추가할 수 있을 때
        else:
            cache.append(city)
            time += 5
            continue
            
    return time