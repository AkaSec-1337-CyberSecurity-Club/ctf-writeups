# Web

# Secret of Konoha

This challenge was pretty straightforward, visiting the url you will be greeted with the following source code

![Screen Shot 2022-10-21 at 12.39.47 PM.png](assets/Screen_Shot_2022-10-21_at_12.39.47_PM.png)

so the first it does is check how many  elements we have the `args` array, then it checks if any of the first two elements are `cat` (we can use `tac` , `head` or `tail` 😏).

Then it executes our whatever we passed in the `args` array.

Let’s try list the root directory :

![Screen Shot 2022-10-21 at 12.55.46 PM.png](assets/Screen_Shot_2022-10-21_at_12.55.46_PM.png)

we can see a secret file, let’s check it’s content:

![Screen Shot 2022-10-21 at 1.00.03 PM.png](assets/Screen_Shot_2022-10-21_at_1.00.03_PM.png)

Looks like a base64, decoding it will give us the flag

```bash
└─$ echo "QUtBU0VDe1czX2M0bl9EMF8xVH0=" | base64 -d
AKASEC{W3_c4n_D0_1T}
```
