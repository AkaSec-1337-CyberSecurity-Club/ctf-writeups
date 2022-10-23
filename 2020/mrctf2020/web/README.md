## PYWebsite

A simple front-end trick question, I hope more people will notice that front-end verification is insecure.

The first step is to go through the business logic, which is the process of purchasing the authorization code and then verifying the authorization code. The loopholes in the audit verification process naturally come to mind. Click the button to pop up the window is controlled by js, and then guess the verification logic is in the front end, so look at the source code and find the logic as follows:


Don't know about MD5? In fact, we don't need to care about the front-end verification at all, we just need to jump directly to flag.php. (md5("ARandomString"))

Enter flag.php, the title tells us that only a specific IP can be accessed, and it is a back-end verification. In fact, it doesn't make sense for the application layer to use XFF to verify IP. PHP uses the X-Forward-For http request header to verify, and this request header we can forge.

We don't know the buyer's IP, but we know the "own" IP, which is the local loopback address 127.0.0.1. Therefore, you only need to use the packet capture software to capture the HTTP request packet and modify it (add X-Forwarded-For: 127.0.0.1a line) to deceive the verification logic. The last flag font I changed to white hhh, so we need to observe the verification logic of the source code backend as follows:

```python
function checkXFF() {
  if(isset($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    if (strpos($ip, "127.0.0.1") !== false) {
      return true;
    }
  }
  return false;
}
```

By the way, how to verify the real IP of the user? It's really not easy to do. Because users may use a proxy (called a forward proxy), our server will also perform forwarding operations such as load balancing (called a reverse proxy) due to business requirements. But if this process is not through a proxy, generally using Remote_Addr can get the real IP. flag:MRCTF{Ba1_Pia0_Flag_1s_ve7y_H4PPY!}


