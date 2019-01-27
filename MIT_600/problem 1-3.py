abc = 'abcdefghijklmnopqrstuvwxyz'
dic = {x:y for x,y in zip(abc, abc[1:])}
s= 'ybtfktefbuf'
tie_result = ""
idx = 0
for i in s:
    in_idx = idx
    result = i
    while in_idx < len(s) - 1:
        if s[in_idx+1] == s[in_idx]:
            result += s[in_idx+1]
            in_idx += 1
        else:
            if s[in_idx] == 'z':
                break
            else:
                daum = dic[s[in_idx]]
                while daum != s[in_idx+1]:
                    if daum == 'z':
                        break
                    daum = dic[daum]
                if daum == s[in_idx + 1]:
                    result += daum
                    in_idx += 1
                else:
                    break
    if len(result) > len(tie_result):
        tie_result = result
                
    idx += 1
    
print("Longest substring in alphabetical order is:", tie_result)