import cookielib
import os
import sys
import time
import urllib2


def init_request(proxy=None):
    handlers = list()
    handlers.append(urllib2.HTTPHandler())

    if proxy:
        proxy_handler = urllib2.ProxyHandler({"http": proxy, "https": proxy})
        handlers.append(proxy_handler)

    cookiejar = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cookiejar)
    handlers.append(cookie_handler)

    opener = urllib2.build_opener(*handlers)
    opener.addheaders = [("User-agent", "Mozilla/5.0")]
    urllib2.install_opener(opener)


def request_response(*req_args, **req_kwargs):
    res = None
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
    debug = False
    if "debug" in req_kwargs:
        debug = req_kwargs["debug"]
        del req_kwargs["debug"]

    starttime = None
    if debug:
        print "req", req_args[0]
        starttime = time.time()

    res = request_response(*req_args, **req_kwargs)

    if debug:
        endtime = time.time() - starttime
        print "res", "%.2fs" % endtime, res.code, res.url

    return res.read()


def request_cached(path, *req_args, **req_kwargs):
    path = checkpath(path)
    if os.path.exists(path):
        return undump(path)
    else:
        content = request(*req_args, **req_kwargs)
        dump(content, path)
        return content


def download_request(path, *req_args, **req_kwargs):
    path = checkpath(path)
    res = request_response(*req_args, **req_kwargs)

    chunksize = 1 << 14
    totaldots = 60

    res_info = res.info()
    res_size = int(res_info.getheaders("Content-Length")[0])
    res_chunks = res_size / chunksize
    out_chunks = 0
    dots_old = 0

    with open(path, "wb") as fout:
        while True:
            chunk = res.read(chunksize)
            if not chunk:
                break
            fout.write(chunk)
            out_chunks += 1
            dots = totaldots * out_chunks / res_chunks

            if dots > dots_old:
                dots_old = dots
                sys.stdout.write(".")
                sys.stdout.flush()
    print " loaded {} bytes".format(res_size)


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
