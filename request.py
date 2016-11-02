import urllib2
import cookielib
import time
import os


def init_request():
    handlers = list()
    handlers.append(urllib2.HTTPHandler())

    cookiejar = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cookiejar)
    handlers.append(cookie_handler)

    opener = urllib2.build_opener(*handlers)
    urllib2.install_opener(opener)


def request_response(*req_args, **req_kwargs):
    req = urllib2.Request(*req_args, **req_kwargs)
    attempt = 1
    while True:
        try:
            res = urllib2.urlopen(req)
            break
        except urllib2.HTTPError:
            print "Retrying after receiving HTTPError...", attempt
            if attempt >= 5:
                raise
            else:
                attempt += 1
    return res


def request(*req_args, **req_kwargs):
    res = request_response(*req_args, **req_kwargs)
    return res.read()


def request_debug(*req_args, **req_kwargs):
    print "req", req_args[0]
    starttime = time.time()
    res = request_response(*req_args, **req_kwargs)
    endtime = time.time() - starttime
    print "res", "%.2fs" % endtime, res.code, res.url
    return res.read()


def checkpath(path):
    if os.sep != "/" and "/" in path:
        path = path.replace("/", os.sep)
    if os.sep in path:
        path_dir = path[:path.rfind(os.sep)]
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
    return path


def dump(content, path):
    path = checkpath(path)
    with open(path, "wb") as fout:
        fout.write(content)


def dump_unicode(content, path):
    if isinstance(content, unicode):
        content = content.encode("utf8")
    dump(content, path)


def undump(path):
    path = checkpath(path)
    with open(path, "rb") as fin:
        content = fin.read()
    return content


def copydump(inpath, outpath):
    fin = open(checkpath(inpath), "rb")
    fout = open(checkpath(outpath), "wb")

    fout.write(fin.read())
    fin.close()
    fout.close()


def request_cached(path, *openargs):
    path = checkpath(path)
    if os.path.exists(path):
        return undump(path)
    else:
        content = request(*openargs)
        dump(content, path)
        return content


def request_cached_debug(path, *openargs):
    path = checkpath(path)
    if os.path.exists(path):
        return undump(path)
    else:
        content = request_debug(*openargs)
        dump(content, path)
        return content
