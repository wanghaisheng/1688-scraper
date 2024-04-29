
function u(e) {
    function t(e, t) {
        return e << t | e >>> 32 - t
    }

    function n(e, t) {
        var n, o, r, i, s;
        return r = 2147483648 & e,
            i = 2147483648 & t,
            n = 1073741824 & e,
            o = 1073741824 & t,
            s = (1073741823 & e) + (1073741823 & t),
            n & o ? 2147483648 ^ s ^ r ^ i : n | o ? 1073741824 & s ? 3221225472 ^ s ^ r ^ i : 1073741824 ^ s ^ r ^ i : s ^ r ^ i
    }

    function o(e, t, n) {
        return e & t | ~e & n
    }

    function r(e, t, n) {
        return e & n | t & ~n
    }

    function i(e, t, n) {
        return e ^ t ^ n
    }

    function s(e, t, n) {
        return t ^ (e | ~n)
    }

    function a(e, r, i, s, a, p, u) {
        return e = n(e, n(n(o(r, i, s), a), u)),
            n(t(e, p), r)
    }

    function p(e, o, i, s, a, p, u) {
        return e = n(e, n(n(r(o, i, s), a), u)),
            n(t(e, p), o)
    }

    function u(e, o, r, s, a, p, u) {
        return e = n(e, n(n(i(o, r, s), a), u)),
            n(t(e, p), o)
    }

    function c(e, o, r, i, a, p, u) {
        return e = n(e, n(n(s(o, r, i), a), u)),
            n(t(e, p), o)
    }

    function d(e) {
        for (var t, n = e.length, o = n + 8, r = (o - o % 64) / 64, i = 16 * (r + 1), s = new Array(i - 1), a = 0, p = 0; n > p;)
            t = (p - p % 4) / 4,
                a = p % 4 * 8,
                s[t] = s[t] | e.charCodeAt(p) << a,
                p++;
        return t = (p - p % 4) / 4,
            a = p % 4 * 8,
            s[t] = s[t] | 128 << a,
            s[i - 2] = n << 3,
            s[i - 1] = n >>> 29,
            s
    }

    function l(e) {
        var t, n, o = "", r = "";
        for (n = 0; 3 >= n; n++)
            t = e >>> 8 * n & 255,
                r = "0" + t.toString(16),
                o += r.substr(r.length - 2, 2);
        return o
    }

    function f(e) {
        e = e.replace(/\r\n/g, "\n");
        for (var t = "", n = 0; n < e.length; n++) {
            var o = e.charCodeAt(n);
            128 > o ? t += String.fromCharCode(o) : o > 127 && 2048 > o ? (t += String.fromCharCode(o >> 6 | 192),
                t += String.fromCharCode(63 & o | 128)) : (t += String.fromCharCode(o >> 12 | 224),
                t += String.fromCharCode(o >> 6 & 63 | 128),
                t += String.fromCharCode(63 & o | 128))
        }
        return t
    }

    var m, h, g, _, y, v, R, S, w, O = [], E = 7, A = 12, q = 17, b = 22, T = 5, x = 9, N = 14, C = 20, k = 4, J = 11,
        P = 16, L = 23, I = 6, D = 10, j = 15, W = 21;
    for (e = f(e),
             O = d(e),
             v = 1732584193,
             R = 4023233417,
             S = 2562383102,
             w = 271733878,
             m = 0; m < O.length; m += 16)
        h = v,
            g = R,
            _ = S,
            y = w,
            v = a(v, R, S, w, O[m + 0], E, 3614090360),
            w = a(w, v, R, S, O[m + 1], A, 3905402710),
            S = a(S, w, v, R, O[m + 2], q, 606105819),
            R = a(R, S, w, v, O[m + 3], b, 3250441966),
            v = a(v, R, S, w, O[m + 4], E, 4118548399),
            w = a(w, v, R, S, O[m + 5], A, 1200080426),
            S = a(S, w, v, R, O[m + 6], q, 2821735955),
            R = a(R, S, w, v, O[m + 7], b, 4249261313),
            v = a(v, R, S, w, O[m + 8], E, 1770035416),
            w = a(w, v, R, S, O[m + 9], A, 2336552879),
            S = a(S, w, v, R, O[m + 10], q, 4294925233),
            R = a(R, S, w, v, O[m + 11], b, 2304563134),
            v = a(v, R, S, w, O[m + 12], E, 1804603682),
            w = a(w, v, R, S, O[m + 13], A, 4254626195),
            S = a(S, w, v, R, O[m + 14], q, 2792965006),
            R = a(R, S, w, v, O[m + 15], b, 1236535329),
            v = p(v, R, S, w, O[m + 1], T, 4129170786),
            w = p(w, v, R, S, O[m + 6], x, 3225465664),
            S = p(S, w, v, R, O[m + 11], N, 643717713),
            R = p(R, S, w, v, O[m + 0], C, 3921069994),
            v = p(v, R, S, w, O[m + 5], T, 3593408605),
            w = p(w, v, R, S, O[m + 10], x, 38016083),
            S = p(S, w, v, R, O[m + 15], N, 3634488961),
            R = p(R, S, w, v, O[m + 4], C, 3889429448),
            v = p(v, R, S, w, O[m + 9], T, 568446438),
            w = p(w, v, R, S, O[m + 14], x, 3275163606),
            S = p(S, w, v, R, O[m + 3], N, 4107603335),
            R = p(R, S, w, v, O[m + 8], C, 1163531501),
            v = p(v, R, S, w, O[m + 13], T, 2850285829),
            w = p(w, v, R, S, O[m + 2], x, 4243563512),
            S = p(S, w, v, R, O[m + 7], N, 1735328473),
            R = p(R, S, w, v, O[m + 12], C, 2368359562),
            v = u(v, R, S, w, O[m + 5], k, 4294588738),
            w = u(w, v, R, S, O[m + 8], J, 2272392833),
            S = u(S, w, v, R, O[m + 11], P, 1839030562),
            R = u(R, S, w, v, O[m + 14], L, 4259657740),
            v = u(v, R, S, w, O[m + 1], k, 2763975236),
            w = u(w, v, R, S, O[m + 4], J, 1272893353),
            S = u(S, w, v, R, O[m + 7], P, 4139469664),
            R = u(R, S, w, v, O[m + 10], L, 3200236656),
            v = u(v, R, S, w, O[m + 13], k, 681279174),
            w = u(w, v, R, S, O[m + 0], J, 3936430074),
            S = u(S, w, v, R, O[m + 3], P, 3572445317),
            R = u(R, S, w, v, O[m + 6], L, 76029189),
            v = u(v, R, S, w, O[m + 9], k, 3654602809),
            w = u(w, v, R, S, O[m + 12], J, 3873151461),
            S = u(S, w, v, R, O[m + 15], P, 530742520),
            R = u(R, S, w, v, O[m + 2], L, 3299628645),
            v = c(v, R, S, w, O[m + 0], I, 4096336452),
            w = c(w, v, R, S, O[m + 7], D, 1126891415),
            S = c(S, w, v, R, O[m + 14], j, 2878612391),
            R = c(R, S, w, v, O[m + 5], W, 4237533241),
            v = c(v, R, S, w, O[m + 12], I, 1700485571),
            w = c(w, v, R, S, O[m + 3], D, 2399980690),
            S = c(S, w, v, R, O[m + 10], j, 4293915773),
            R = c(R, S, w, v, O[m + 1], W, 2240044497),
            v = c(v, R, S, w, O[m + 8], I, 1873313359),
            w = c(w, v, R, S, O[m + 15], D, 4264355552),
            S = c(S, w, v, R, O[m + 6], j, 2734768916),
            R = c(R, S, w, v, O[m + 13], W, 1309151649),
            v = c(v, R, S, w, O[m + 4], I, 4149444226),
            w = c(w, v, R, S, O[m + 11], D, 3174756917),
            S = c(S, w, v, R, O[m + 2], j, 718787259),
            R = c(R, S, w, v, O[m + 9], W, 3951481745),
            v = n(v, h),
            R = n(R, g),
            S = n(S, _),
            w = n(w, y);
    var H = l(v) + l(R) + l(S) + l(w);
    return H.toLowerCase()
}
// console.log(a)
// console.log(p)

// var e='5970c860dcff67864c7b1912bd984ee9&1602670696727&12574478&{"cid":"TpFacCoreInfosService:TpFacCoreInfosService","methodName":"execute","params":"{\"facAliId\":\"2019106328\"}"}'
// var e='87ce3da8b6f5218713fc35e8b9d9d7de&1602738209823&12574478&{"cid":"TpFacCoreInfosService:TpFacCoreInfosService","methodName":"execute","params":"{\\"facAliId\\":\\"2019106328\\"}"}'
// var a = (new Date).getTime()
// // var a='1602810824704'
// var s='12574478'
// var token='8a0539ff99e9241f36538eee5f490e48'
// var data='{"cid":"TpFacCoreInfosService:TpFacCoreInfosService","methodName":"execute","params":"{\\"facAliId\\":\\"2019106328\\"}"}'
//
// p = (token + "&" + a + "&" + s + "&" + data)
// console.log(a)
// console.log(u(p))
