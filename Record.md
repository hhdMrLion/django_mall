# 未填的坑
#### 个人模块
```text
个人收货地址管理，点添加后显示异常
```
#### 商品模块
```text
在除了375*667分辨率下，下拉刷新列表，有个page=3 404 错误，看不到下面更多的商品
在375*667（iPhone6/7/8）显示正常
（应该窗口的大小没有适应图片的大小，导致了一列的商品没有铺满整个屏幕，导致页面有额外空间，
程序会以此要加载数据填补空间，导致了page=3的错误）
```
#### xadmin
```text
django缺少reversion模块，添加上迁移数据库时会报错，提示出现字长过长的错误，于是先删掉
```