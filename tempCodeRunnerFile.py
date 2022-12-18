 else:
            if read == 'on':
                read=1
                if url in cat_url_set:
                    i = cat_url_set.index(url)
                    visited[i] = 1