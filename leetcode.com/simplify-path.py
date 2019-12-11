class Solution:
    def simplifyPath(self, path: str) -> str:
        sp = path.split('/')
        st = []
        for i in range(len(sp)):
            token = sp[i]
            #print(token)
            if token == '..':
                if st:
                    st.pop()
            elif token == '.':
                continue
            elif token:
                st.append(token)
        res = '/'
        while st:
            res = '/'+ st.pop() + res
        if len(res)>1 and res[-1] =='/':
            res = res[:-1] 
        return res 

if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/../"))#"/"
    print(s.simplifyPath("/home//foo/"))#"/home/foo"
    print(s.simplifyPath("/a/./b/../../c/"))#"/c"
    print(s.simplifyPath("/a/../../b/../c//.//"))#"/c"
    print(s.simplifyPath("/a//b////c/d//././/.."))#"/a/b/c"
    