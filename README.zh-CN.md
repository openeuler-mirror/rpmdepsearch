# rpmdepsearch-软件包被依赖关系查询


通过维护rpm源的数据，实现软件包被依赖关系的查询。


## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用说明](#使用说明)
- [维护者](#维护者)
- [使用许可](#使用许可)

## 背景

本仓库是开源之夏2023的项目。

## 安装

这个项目使用 python3 编写，运行前请保证运行环境完整。
软件包可以使用rpm软件包安装，仓库内有安装用的spec文件。

## 使用说明

首次使用前需要在配置文件内配置监控的软件仓库链接，路径在%{_sysconfdir}/rpmdepsearch/rpmdepsearch.conf下，%{_sysconfdir}是rpm提供的系统配置文件夹。
之后可以使用rpmdepsearch setup来更新监控数据。监控数据只能手动更新。之后可以使用如下命令查询软件包被依赖关系：

```sh
$ rpmdepsearch rpm
# Prints out packages that require rpm
$ rpmdepsearch rpm python
# Muti queries
```




## 维护者

[@Zoar_yalz](https://gitee.com/Zoar_yalz)。
由于是首次参与开源项目，问题在所难免。希望您可以提交PR或Issue来指正，非常感谢您的支持！



## 使用许可
[MulanPSL-2.0](https://gitee.com/openeuler/A-Tune/blob/master/License/LICENSE#)
