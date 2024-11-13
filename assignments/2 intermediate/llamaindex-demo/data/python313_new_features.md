Python 3.13 有什么新变化 — Python 3.14.0a1 文档             @media only screen { table.full-width-table { width: 100%; } }   

[![Python logo](../_static/py.svg)](https://www.python.org/)

Theme Auto Light Dark

### [目录](../contents.html)

*   [Python 3.13 有什么新变化](#)
   *   [摘要 -- 发布重点](#summary-release-highlights)
   *   [新的特性](#new-features)
       *   [更好的交互式解释器](#a-better-interactive-interpreter)
       *   [改进的错误消息](#improved-error-messages)
       *   [自由线程的 CPython](#free-threaded-cpython)
       *   [实验性的即时 (JIT) 编译器](#an-experimental-just-in-time-jit-compiler)
       *   [针对 `locals()` 的已定义修改语义](#defined-mutation-semantics-for-locals)
       *   [对移动平台的支持](#support-for-mobile-platforms)
   *   [其他语言特性修改](#other-language-changes)
   *   [新增模块](#new-modules)
   *   [改进的模块](#improved-modules)
       *   [argparse](#argparse)
       *   [array](#array)
       *   [ast](#ast)
       *   [asyncio](#asyncio)
       *   [base64](#base64)
       *   [compileall](#compileall)
       *   [concurrent.futures](#concurrent-futures)
       *   [configparser](#configparser)
       *   [copy](#copy)
       *   [ctypes](#ctypes)
       *   [dbm](#dbm)
       *   [dis](#dis)
       *   [doctest](#doctest)
       *   [email](#email)
       *   [fractions](#fractions)
       *   [glob](#glob)
       *   [importlib](#importlib)
       *   [io](#io)
       *   [ipaddress](#ipaddress)
       *   [itertools](#itertools)
       *   [marshal](#marshal)
       *   [math](#math)
       *   [mimetypes](#mimetypes)
       *   [mmap](#mmap)
       *   [multiprocessing](#multiprocessing)
       *   [os](#os)
       *   [os.path](#os-path)
       *   [pathlib](#pathlib)
       *   [pdb](#pdb)
       *   [queue](#queue)
       *   [random](#random)
       *   [re](#re)
       *   [shutil](#shutil)
       *   [site](#site)
       *   [sqlite3](#sqlite3)
       *   [ssl](#ssl)
       *   [statistics](#statistics)
       *   [subprocess](#subprocess)
       *   [sys](#sys)
       *   [tempfile](#tempfile)
       *   [time](#time)
       *   [tkinter](#tkinter)
       *   [回溯](#traceback)
       *   [types](#types)
       *   [typing](#typing)
       *   [unicodedata](#unicodedata)
       *   [venv](#venv)
       *   [warnings](#warnings)
       *   [xml](#xml)
       *   [zipimport](#zipimport)
   *   [性能优化](#optimizations)
   *   [被移除的模块与 API](#removed-modules-and-apis)
       *   [PEP 594: 从标准库中移除“死电池”](#pep-594-remove-dead-batteries-from-the-standard-library)
       *   [2to3](#to3)
       *   [builtins](#builtins)
       *   [configparser](#id3)
       *   [importlib.metadata](#importlib-metadata)
       *   [locale](#locale)
       *   [opcode](#opcode)
       *   [pathlib](#id4)
       *   [re](#id5)
       *   [tkinter.tix](#tkinter-tix)
       *   [turtle](#turtle)
       *   [typing](#id6)
       *   [unittest](#unittest)
       *   [urllib](#urllib)
       *   [webbrowser](#webbrowser)
   *   [新的弃用](#new-deprecations)
       *   [Pending removal in Python 3.14](#pending-removal-in-python-3-14)
       *   [Pending removal in Python 3.15](#pending-removal-in-python-3-15)
       *   [Pending removal in Python 3.16](#pending-removal-in-python-3-16)
       *   [Pending removal in future versions](#pending-removal-in-future-versions)
   *   [CPython 字节码的变化](#cpython-bytecode-changes)
   *   [C API 的变化](#c-api-changes)
       *   [新的特性](#id7)
       *   [被改变的 C API](#changed-c-apis)
       *   [受限 C API 的改变](#limited-c-api-changes)
       *   [Removed C APIs](#removed-c-apis)
       *   [已弃用的 C API](#deprecated-c-apis)
           *   [Pending removal in Python 3.14](#id8)
           *   [Pending removal in Python 3.15](#id9)
           *   [Pending removal in future versions](#id10)
   *   [构建变化](#build-changes)
   *   [Porting to Python 3.13](#porting-to-python-3-13)
       *   [Python API 的变化](#changes-in-the-python-api)
       *   [C API 的变化](#changes-in-the-c-api)
   *   [回归测试的变化](#regression-test-changes)

#### 上一主题

[What's new in Python 3.14](3.14.html "上一章")

#### 下一主题

[Python 3.12 有什么新变化](3.12.html "下一章")

### 当前页

*   [报告 Bug](../bugs.html)
*   [显示源码](https://github.com/python/cpython/blob/main/Doc/whatsnew/3.13.rst)

### 导航

*   [索引](../genindex.html "总索引")
*   [模块](../py-modindex.html "Python 模块索引") |
*   [下一页](3.12.html "Python 3.12 有什么新变化") |
*   [上一页](3.14.html "What's new in Python 3.14") |
*   ![Python logo](../_static/py.svg)
*   [Python](https://www.python.org/) »

*   [3.14.0a1 Documentation](../index.html) »
*   [Python的新变化](index.html) »
*   Python 3.13 有什么新变化
*    
   
   |
*   Theme Auto Light Dark |

Python 3.13 有什么新变化[¶](#what-s-new-in-python-3-13 "Link to this heading")
========================================================================

编者:

Adam Turner 和 Thomas Wouters

本文介绍了 Python 3.13 相比 3.12 增加的新我。 Python 3.13 已于 2024 年 10 月 7 日发布。 要获取详细信息，可参阅 [更新日志](changelog.html#changelog)。

参见

[**PEP 719**](https://peps.python.org/pep-0719/) -- Python 3.13 发布计划

摘要 -- 发布重点[¶](#summary-release-highlights "Link to this heading")
-----------------------------------------------------------------

Python 3.13 是 Python 编程语言的最新稳定发布版，包含多项针对语言、实现和标准库的改变。 最大的变化包括一个新的 [交互式解释器](#whatsnew313-better-interactive-interpreter)，以及对于在 [自由线程模式](#whatsnew313-free-threaded-cpython) ([**PEP 703**](https://peps.python.org/pep-0703/)) 下运行和 [即时编译器](#whatsnew313-jit-compiler) ([**PEP 744**](https://peps.python.org/pep-0744/)) 的实验性支持。

错误消息继续得到改进，回溯信息现在默认使用彩色高亮显示。 [`locals()`](../library/functions.html#locals "locals") 内置函数现在对于修改所返回的映射具有 [更细化的语法](#whatsnew313-locals-semantics)，并且类型形参现在支持设置默认值。

针对标准库的改变包括移除已弃用的 API 和模块，以及用户友好度和正确性方面的常规提升。 一些旧式标准库模块自 Python 3.11 起被弃用 ([**PEP 594**](https://peps.python.org/pep-0594/)) 之后现在 [已被移除](#whatsnew313-pep594)。

本文并不试图提供所有新特性的完整规范说明，而是提供一个方便的概览。 要了解完整细节请参阅相应文档，如 [标准库参数](../library/index.html#library-index) 和 [语言参考](../reference/index.html#reference-index)。 要了解某项改变的完整实现和设计理念，请参阅相应新特性的 PEP；但请注意一旦某项特性已完全实现则相应 PEP 通常不会再继续更新。 请参阅 [迁移到 Python 3.13](#porting-to-python-3-13) 了解如何从较早 Python 进行升级的指导。

* * *

解释器的改进：

*   大幅改进的 [交互式解释器](#whatsnew313-better-interactive-interpreter) 和 [改进的错误消息](#whatsnew313-improved-error-messages)。
   
*   [**PEP 667**](https://peps.python.org/pep-0667/): 现在 [`locals()`](../library/functions.html#locals "locals") 内置函数在修改被返回的映射时具有 [已定义语义](#whatsnew313-locals-semantics)。 Python 调试器及类似的工具现在即使在并发代码执行期间也能更可靠地在已优化的作用域中更新局部变量。
   
*   [**PEP 703**](https://peps.python.org/pep-0703/): CPython 3.13 具有对在运行时禁用 [global interpreter lock](../glossary.html#term-global-interpreter-lock) 的实验性支持。 请参阅 [自由线程 CPython](#whatsnew313-free-threaded-cpython) 了解详情。
   
*   [**PEP 744**](https://peps.python.org/pep-0744/): 增加了一个基本的 [JIT 编译器](#whatsnew313-jit-compiler)。 目前默认是禁用的（但以后可能启用）。 能够小幅提升性能 -- 我们预计在接下来的几个发布版中不断改进它。
   
*   在新的 [交互式解释器](#whatsnew313-better-interactive-interpreter) 中，以及 [回溯信息](#whatsnew313-improved-error-messages) 和 [文档测试](#whatsnew313-doctest) 输出中的颜色支持。 这可以通过 [`PYTHON_COLORS`](../using/cmdline.html#envvar-PYTHON_COLORS) and [`NO_COLOR`](https://no-color.org/) 环境变量来禁用。
   

对 Python 数据模型的改进：

*   [`__static_attributes__`](../reference/datamodel.html#type.__static_attributes__ "type.__static_attributes__") 保存了可在一个类体的任何函数中通过 `self.X` 来访问的属性名称。
   
*   [`__firstlineno__`](../reference/datamodel.html#type.__firstlineno__ "type.__firstlineno__") 记录了一个类定义的首行的行号。
   

标准库中的重大改进：

*   新增了 [`PythonFinalizationError`](../library/exceptions.html#PythonFinalizationError "PythonFinalizationError") 异常，当操作在 [最终化](../glossary.html#term-interpreter-shutdown) 期间被阻塞时将被引发。
   
*   现在 [`argparse`](../library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.") 模块可支持弃用命令行选项、位置参数和子命令。
   
*   新增的函数 [`base64.z85encode()`](../library/base64.html#base64.z85encode "base64.z85encode") 和 [`base64.z85decode()`](../library/base64.html#base64.z85decode "base64.z85decode") 支持对 [Z85 数据](https://rfc.zeromq.org/spec/32/) 进行编码和解码。
   
*   现在 [`copy`](../library/copy.html#module-copy "copy: Shallow and deep copy operations.") 模块有一个 [`copy.replace()`](../library/copy.html#copy.replace "copy.replace") 函数，支持许多内置类型和任何定义了 [`__replace__()`](../library/copy.html#object.__replace__ "object.__replace__") 方法的类。
   
*   新的 [`dbm.sqlite3`](../library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm (All)") 模块现在是默认的 [`dbm`](../library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats.") 后端。
   
*   [`os`](../library/os.html#module-os "os: Miscellaneous operating system interfaces.") 模块增加了 [一套新函数](../library/os.html#os-timerfd) 用于处理 Linux 的定时器通知文件描述符。
   
*   现在 [`random`](../library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") 模块提供了一个 [命令行界面](../library/random.html#random-cli)。
   

安全改进：

*   [`ssl.create_default_context()`](../library/ssl.html#ssl.create_default_context "ssl.create_default_context") 设置了 [`ssl.VERIFY_X509_PARTIAL_CHAIN`](../library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN "ssl.VERIFY_X509_PARTIAL_CHAIN") 和 [`ssl.VERIFY_X509_STRICT`](../library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT") 作为默认的旗标。
   

C API 的改进：

*   现在 [`Py_mod_gil`](../c-api/module.html#c.Py_mod_gil "Py_mod_gil") 槽位被用来指明一个扩展模块支持在禁用 [GIL](../glossary.html#term-GIL) 的情况下运行。
   
*   增加了 [PyTime C API](../c-api/time.html)，提供了对系统时钟的访问。
   
*   [`PyMutex`](../c-api/init.html#c.PyMutex "PyMutex") 是新增的轻量级互斥锁，只占用一个字节。
   
*   新增了 [一套函数](../c-api/monitoring.html#c-api-monitoring) 用于在 C API 中生成 [**PEP 669**](https://peps.python.org/pep-0669/) 监控事件。
   

新的类型标注特性：

*   [**PEP 696**](https://peps.python.org/pep-0696/): 类型形参 ([`typing.TypeVar`](../library/typing.html#typing.TypeVar "typing.TypeVar"), [`typing.ParamSpec`](../library/typing.html#typing.ParamSpec "typing.ParamSpec") 和 [`typing.TypeVarTuple`](../library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple")) 现在可支持默认值。
   
*   [**PEP 702**](https://peps.python.org/pep-0702/): 新的 [`warnings.deprecated()`](../library/warnings.html#warnings.deprecated "warnings.deprecated") 装饰器在类型系统和运行时中增加了对标记为弃用的支持。
   
*   [**PEP 705**](https://peps.python.org/pep-0705/): [`typing.ReadOnly`](../library/typing.html#typing.ReadOnly "typing.ReadOnly") 可被用来将 [`typing.TypedDict`](../library/typing.html#typing.TypedDict "typing.TypedDict") 的项标记为对类型检查器只读。
   
*   [**PEP 742**](https://peps.python.org/pep-0742/): [`typing.TypeIs`](../library/typing.html#typing.TypeIs "typing.TypeIs") 提供了更直观的类型细化行为，作为对 [`typing.TypeGuard`](../library/typing.html#typing.TypeGuard "typing.TypeGuard") 的替代。
   

平台支持：

*   [**PEP 730**](https://peps.python.org/pep-0730/): 现在 Apple 的 iOS 是 [官方支持的平台](#whatsnew313-platform-support)，处于 [**第 3 层级**](https://peps.python.org/pep-0011/#tier-3)。
   
*   [**PEP 738**](https://peps.python.org/pep-0738/): 现在 Android 是 [官方支持的平台](#whatsnew313-platform-support)，处于 [**第 3 层级**](https://peps.python.org/pep-0011/#tier-3)。
   
*   现在 `wasm32-wasi` 作为 [**第 2 层级**](https://peps.python.org/pep-0011/#tier-2) 的平台受到支持。
   
*   `wasm32-emscripten` 不再是受到官方支持的平台。
   

重要的移除：

*   [PEP 594](#whatsnew313-pep594): 剩余的 19 个“死电池”（老旧 stdlib 模块）已从标准库中移除: `aifc`, `audioop`, `cgi`, `cgitb`, `chunk`, `crypt`, `imghdr`, `mailcap`, `msilib`, `nis`, `nntplib`, `ossaudiodev`, `pipes`, `sndhdr`, `spwd`, `sunau`, `telnetlib`, `uu` 和 `xdrlib`。
   
*   移除了 **2to3** 工具和 `lib2to3` 模块（在 Python 3.11 中已被弃用）。
   
*   移除了 `tkinter.tix` 模块（在 Python 3.6 中已被弃用）。
   
*   移除了 `locale.resetlocale()` 函数。
   
*   移除了 `typing.io` 和 `typing.re` 命名空间。
   
*   移除了链式的 [`classmethod`](../library/functions.html#classmethod "classmethod") 描述器。
   

发布计划的变化：

[**PEP 602**](https://peps.python.org/pep-0602/) ("Annual Release Cycle for Python") 已被更新为将新发布版的完整支持 ('bugfix') 期扩展至两年。 这个更新的政策意味着：

*   Python 3.9--3.12 有一年半的完整支持，另加三年半的安全修正。
   
*   Python 3.13 及以后的版本有两年的完整支持，另加三年的安全修正。
   

新的特性[¶](#new-features "Link to this heading")
---------------------------------------------

### 更好的交互式解释器[¶](#a-better-interactive-interpreter "Link to this heading")

Python 现在默认会使用新的 [interactive](../glossary.html#term-interactive) shell，它基于来自 [PyPy 项目](https://pypy.org/) 的代码。 当使用从交互式终端启动 [REPL](../glossary.html#term-REPL) 时，下列新特性将受到支持：

*   多行编辑并保留历史记录。
   
*   对 REPL 专属的命令如 help, exit 和 quit 的直接支持，无需以函数形式调用它们。
   
*   提示和回溯 [默认启用彩色显示](../using/cmdline.html#using-on-controlling-color)。
   
*   使用 F1 浏览交互式帮助并带有单独的命令历史。
   
*   使用 F2 浏览去除了输出以及 [\>>>](../glossary.html#term-0) 和 [...](../glossary.html#term-...) 提示符的历史。
   
*   使用 F3 进入“粘贴模式”以更方便地粘贴大段代码（再次按 F3 返回常规提示符）。
   

要禁用新的交互式 shell，可设置 [`PYTHON_BASIC_REPL`](../using/cmdline.html#envvar-PYTHON_BASIC_REPL) 环境变量。 有关交互模式的详情，请参见 [交互模式](../tutorial/appendix.html#tut-interac)。

（由 Pablo Galindo Salgado, Łukasz Langa 和 Lysandros Nikolaou 在 [gh-111201](https://github.com/python/cpython/issues/111201) 基于来自 PyPy 项目的代码贡献。 Windows 支持由 Dino Viehland 和 Anthony Shaw 贡献。）

### 改进的错误消息[¶](#improved-error-messages "Link to this heading")

*   在终端里显示回溯时解释器现在会默认使用彩色。 此特性可通过新的 [`PYTHON_COLORS`](../using/cmdline.html#envvar-PYTHON_COLORS) 环境变量以及传统的 [`NO_COLOR`](https://no-color.org/) 和 [`FORCE_COLOR`](https://force-color.org/) 环境变量来 [进行控制](../using/cmdline.html#using-on-controlling-color)。 （由 Pablo Galindo Salgado 在 [gh-112730](https://github.com/python/cpython/issues/112730) 中贡献。）
   

*   一个常见错误是撰写的脚本和标准库中的某个模块重名。现在出现此类错误时会显示一条更有用的错误信息：
   
   $ python random.py
   Traceback (most recent call last):
     File "/home/me/random.py", line 1, in <module>
       import random
     File "/home/me/random.py", line 3, in <module>
       print(random.randint(5))
             ^^^^^^^^^^^^^^
   AttributeError: module 'random' has no attribute 'randint' (consider renaming '/home/me/random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
   
   类似地，如果一个脚本具有与它尝试导入的第三方模块相同的名称并因此导致错误，我们也会显示一条更有帮助的错误消息：
   
   $ python numpy.py
   Traceback (most recent call last):
     File "/home/me/numpy.py", line 1, in <module>
       import numpy as np
     File "/home/me/numpy.py", line 3, in <module>
       np.array(\[1, 2, 3\])
       ^^^^^^^^
   AttributeError: module 'numpy' has no attribute 'array' (consider renaming '/home/me/numpy.py' if it has the same name as a library you intended to import)
   
   (由 Shantanu Jain 在 [gh-95754](https://github.com/python/cpython/issues/95754) 中贡献）。
   
*   现在当向一个函数传入不正确的关键字参数时错误消息会尝试提示正确的关键字参数。
   
   \>>> "Better error messages!".split(max\_split\=1)
   Traceback (most recent call last):
     File "<python-input-0>", line 1, in <module>
       "Better error messages!".split(max\_split\=1)
       \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
   TypeError: split() got an unexpected keyword argument 'max\_split'. Did you mean 'maxsplit'?
   
   （由 Pablo Galindo Salgado 和 Shantanu Jain 在 [gh-107944](https://github.com/python/cpython/issues/107944) 中贡献。）
   

### 自由线程的 CPython[¶](#free-threaded-cpython "Link to this heading")

现在 CPython 具有对运行于禁用 [global interpreter lock](../glossary.html#term-global-interpreter-lock) (GIL) 的自由线程模式的实验性支持。 这是一个实验性的特性因而默认是不启用的。 自由线程模式需要一个不同的可执行程序，通常名为 `python3.13t` 或 `python3.13t.exe`。 标记为 _free-threaded_ 的预构建二进制文件可作为官方 [Windows](../using/windows.html#install-freethreaded-windows) 和 [macOS](../using/mac.html#install-freethreaded-macos) 安装器的一部分被安装，或者可以附带 [`--disable-gil`](../using/configure.html#cmdoption-disable-gil) 选项使用源代码来构建 CPython。

自由线程模式的执行允许在可用的 CPU 核心上并行地运行线程从而充分利用可用的处理能力。 虽然并非所有软件都能自动从中受益，但在设计时将线程纳入考虑的程序在多核心硬件上运行速度会更快。 **自由线程模式是实验性的** 并且处于不断改进的过程中：预计会出现一些程序错误并且在单线程场景下出现明显的性能损失。 可以选择使用环境变量 [`PYTHON_GIL`](../using/cmdline.html#envvar-PYTHON_GIL) 或命令行选项 [`-X gil=1`](../using/cmdline.html#cmdoption-X) 让 CPython 的自由线程构建版支持在运行时启用 GIL。

为了检查当前解释器是否支持自由线程，[`python -VV`](../using/cmdline.html#cmdoption-V) 和 [`sys.version`](../library/sys.html#sys.version "sys.version") 将包含 "experimental free-theading build" 字样。 可以使用新增的 `sys._is_gil_enabled()` 函数来检查正在运行的线程是否确实禁用了 GIL。

C-API 扩展模块需要针对自由线程构建版专门进行构建。 支持在禁用 [GIL](../glossary.html#term-GIL) 的情况下运行的扩展应当使用 [`Py_mod_gil`](../c-api/module.html#c.Py_mod_gil "Py_mod_gil") 槽位。 使用单阶段初始化的扩展应当使用 [`PyUnstable_Module_SetGIL()`](../c-api/module.html#c.PyUnstable_Module_SetGIL "PyUnstable_Module_SetGIL") 来指明它们是支支持在禁用 GIL 的情况下运行。 导入不使用这些机制的 C 扩展将导致 GIL 被启用，除非通过 [`PYTHON_GIL`](../using/cmdline.html#envvar-PYTHON_GIL) 环境变量或 [`-X gil=0`](../using/cmdline.html#cmdoption-X) 选项显式地禁用 GIL。 需要 pip 24.1 或更新的版本才能在自由线程构建版中安装带有 C 扩展的软件包。

这项工作成为可能要感谢许多个人和组织，包括针对 Python 和第三方项目测试并启用自由线程支持的庞大的贡献者社区。 重要的贡献者包括：Sam Gross, Ken Jin, Donghee Na, Itamar Oren, Matt Page, Brett Simmers, Dino Viehland, Carl Meyer, Nathan Goldbaum, Ralf Gommers, Lysandros Nikolaou 及其他许多人。 有许多贡献者受雇于 Meta，该公司提供了大量的工程资源来支持此项目。

参见

[**PEP 703**](https://peps.python.org/pep-0703/) "Making the Global Interpreter Lock Optional in CPython" 中包含了有关此项工作的理念和信息。

[Porting Extension Modules to Support Free-Threading](https://py-free-threading.github.io/porting/): 一份由社区维护的针对扩展开发者的移植指南。

### 实验性的即时 (JIT) 编译器[¶](#an-experimental-just-in-time-jit-compiler "Link to this heading")

当 CPython 使用 `--enable-experimental-jit` 选项进行配置和构建时，会添加一个即时（JIT）编译器以加快某些 Python 程序的运行速度。 在 Windows 上，可使用 `PCbuild/build.bat --experimental-jit` 启用 JIT 或使用 `--experimental-jit-interpreter` 启用第 2 层级解释器。 构建要求和进一步的支持信息 [包含在](https://github.com/python/cpython/blob/main/Tools/jit/README.md) `Tools/jit/README.md` 中。

`--enable-experimental-jit` 选项接受这些（可选）值，如果不带可选值地预设 `--enable-experimental-jit` 则默认为 `yes`。

*   `no`: 禁用整个第 2 层级和 JIT 管线。
   
*   `yes`: 启用 JIT。 要在运行时禁用 JIT，则传入环境变量 `PYTHON_JIT=0`。
   
*   `yes-off`: 构建 JIT 但默认禁用它。 要在运行时启用 JIT，则传入环境变量 `PYTHON_JIT=1`。
   
*   `interpreter`: 启用第 2 层级解释器但是禁用 JIT。 可以在运行时传入 `PYTHON_JIT=0` 来禁用该解释器。
   

其内部架构大致如下：

*   我们将从特化的 _第 1 层级字节码_ 开始。 请参阅 [3.11 有什么新变化](3.11.html#whatsnew311-pep659) 了解详情。
   
*   当第 1 层级字节码达到足够热度，它将被翻译为新的纯内部的中间表示形式 (IR)，称为 _第 2 层级 IR_，有时也称为微操作码 ("uops")。
   
*   第 2 层级 IR 使用与第 1 层级相同的基于栈的虚拟机，但其指令格式更适合被翻译为机器码。
   
*   在第 2 层级 IR 被解释或翻译为机器码之前，我们会预先应用一些优化通路。
   
*   虽然第 2 层级解释器存在，但它主要用于对优化管线的先前阶段进行调试。可通过为 Python 配置 `--enable-experimental-jit=interpreter` 选项启用第 2 层级解释器。
   
*   启用 JIT 时，经优化的第 2 层级 IR 将被翻译为机器码后再执行。
   
*   这个机器码翻译过程使用了名为 _拷贝并打补丁_ 的技巧。 它没有运行时依赖，但增加了构建时对 LLVM 的依赖。
   

参见

[**PEP 744**](https://peps.python.org/pep-0744/)

（JIT 来自 Brandt Bucher 且受到 Haoran Xu 和 Fredrik Kjolstad 论文的启发。第 2 层级 IR 来自 Mark Shannon 和 Guido van Rossum。第 2 层级解释器来自 Ken Jin。）

### 针对 [`locals()`](../library/functions.html#locals "locals") 的已定义修改语义[¶](#defined-mutation-semantics-for-locals "Link to this heading")

在历史上，改变 [`locals()`](../library/functions.html#locals "locals") 的返回值的预期结果是留给具体的 Python 实现来定义的。 从 Python 3.13 开始，[**PEP 667**](https://peps.python.org/pep-0667/) 标准化了 CPython 对于大多数代码执行作用域的历史行为，但也将 [已优化作用域](../glossary.html#term-optimized-scope) (函数、生成器、协程、推导式和生成器表达式) 修改为显式地返回当前已赋值的局部变量的独立快照，包括局部引用的在闭包中捕获的非局部变量。

在已优化作用域中对 [`locals()`](../library/functions.html#locals "locals") 语义的这项修改也会影响隐式地以 `locals()` 为目标的代码执行函数的默认行为，如果没有提供显式命名空间的话（例如 [`exec()`](../library/functions.html#exec "exec") 和 [`eval()`](../library/functions.html#eval "eval") 等）。 在之前的版本中，在调用代码执行函数后是否可以通过调用 `locals()` 访问更改情况取决于具体的实现。 具体到 CPython 而言，此类代码通常会按预期工作，但有时可能会在基于其他代码（包括调试器和代码执行跟踪工具）的已优化作用域中失败，因为代码有可能重置该作用域中的共享快照。 现在，代码在已优化作用域中将始终针对局部变量的独立快照运行，因为在后续调用 `locals()` 时将永远看不到更改。 要访问在这些情况下所做的更改，现在必须将一个显式命名空间引用传递给相关的函数。 或者，也可以更新受影响的代码以使用更高层级的代码执行 API 返回结果代码命名空间（例如，当执行磁盘上的 Python 文件时使用 [`runpy.run_path()`](../library/runpy.html#runpy.run_path "runpy.run_path") 函数）。

为确保调试器和类似工具能可靠地更新受到此变化影响的作用域中的局部变量，现在 [`FrameType.f_locals`](../reference/datamodel.html#frame.f_locals "frame.f_locals") 将返回一个针对此种作用域中的帧的局部变量和在局部引用的非局部变量的直通写入代理对象，而不是返回一个非持续更新的具有规定义的运行时语义的共享 `dict` 实例。

请参阅 [**PEP 667**](https://peps.python.org/pep-0667/) 了解详情，包括相关的 C API 更改和弃用。 下文还针对受影响的 [Python API](#pep667-porting-notes-py) 和 [C API](#pep667-porting-notes-c) 提供了移植说明。

（PEP 和实现由 Mark Shannon 和 Tian Gao 在 [gh-74929](https://github.com/python/cpython/issues/74929) 中贡献。 文档更新由 Guido van Rossum 和 Alyssa Coghlan 提供。）

### 对移动平台的支持[¶](#support-for-mobile-platforms "Link to this heading")

[**PEP 730**](https://peps.python.org/pep-0730/): iOS 现在是 [**PEP 11**](https://peps.python.org/pep-0011/) 所支持的平台，包括第 3 层级的 `arm64-apple-ios` 和 `arm64-apple-ios-simulator` 等目标（分别为2013 年后的 iPhone 和 iPad 设备以及运行于 Apple silicon 硬件的 Xcode iOS 模拟器）。 `x86_64-apple-ios-simulator` （运行于较旧的 `x86_64` 硬件的 Xcode iOS 模拟器）不是第 3 层级的受支持平台，但也将尽可能地支持。 （PEP 撰写及实现由 Russell Keith-Magee 在 [gh-114099](https://github.com/python/cpython/issues/114099) 中贡献。）.)

[**PEP 738**](https://peps.python.org/pep-0738/): Android 现在是 [**PEP 11**](https://peps.python.org/pep-0011/) 所支持的平台，包括位于第 3 层级的 `aarch64-linux-android` 和 `x86_64-linux-android` 等目标。 32 位的目标 `arm-linux-androideabi` 和 `i686-linux-android` 不是第 3 层级的受支持平台，但也将尽可能地支持。 （PEP 撰写及实现由 Malcolm Smith 在 [gh-116622](https://github.com/python/cpython/issues/116622) 中贡献。）

参见

[**PEP 730**](https://peps.python.org/pep-0730/), [**PEP 738**](https://peps.python.org/pep-0738/)

其他语言特性修改[¶](#other-language-changes "Link to this heading")
-----------------------------------------------------------

*   编译器现在将从文档字符串的每一行去除共有的前导空格。 这会减少 [字节码缓存](../glossary.html#term-bytecode) 的大小（例如 `.pyc` 文件），例如在 SQLAlchemy 2.0 的 `sqlalchemy.orm.session` 中文件大小将减少约 5%。 这项改变将影响各种使用了文档字符串的工具，如 [`doctest`](../library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")。
   
   \>>> def spam():
   ... """
   ...         This is a docstring with
   ...           leading whitespace.
   ...
   ...         It even has multiple paragraphs!
   ...     """
   ...
   \>>> spam.\_\_doc\_\_
   '\\nThis is a docstring with\\n  leading whitespace.\\n\\nIt even has multiple paragraphs!\\n'
   
   （由 Inada Naoki 在 [gh-81283](https://github.com/python/cpython/issues/81283) 中贡献。）
   
*   类作用域内的 [标注作用域](../reference/executionmodel.html#annotation-scopes) 现在可以包含 lambda 和推导式。 位于类作用域内的推导式不会内联到其父作用域中。
   
   class C\[T\]:
       type Alias \= lambda: T
   
   （由 Jelle Zijlstra 在 [gh-109118](https://github.com/python/cpython/issues/109118) 和 [gh-118160](https://github.com/python/cpython/issues/118160) 中贡献。）
   
*   [future 语句](../reference/simple_stmts.html#future) 不再会被 [`__future__`](../library/__future__.html#module-__future__ "__future__: Future statement definitions") 模块的相对导入触发，意味着 `from .__future__ import ...` 形式的语句现在只是标准的相对导入，而不会激活任何特殊特性。 （由 Jeremiah Gabriel Pascual 在 [gh-118216](https://github.com/python/cpython/issues/118216) 中贡献。）
   
*   现在 [`global`](../reference/simple_stmts.html#global) 声明当其被用于 [`else`](../reference/compound_stmts.html#else) 代码块中时也将被允许在 [`except`](../reference/compound_stmts.html#except) 代码块中使用。 在之前版本中这会错误地引发 [`SyntaxError`](../library/exceptions.html#SyntaxError "SyntaxError")。 （由 Irit Katriel 在 [gh-111123](https://github.com/python/cpython/issues/111123) 中贡献。）
   
*   增加了新的环境变量 [`PYTHON_FROZEN_MODULES`](../using/cmdline.html#envvar-PYTHON_FROZEN_MODULES)，它确定冻结模块是否会被导入机制所忽略，等价于 [`-X frozen_modules`](../using/cmdline.html#cmdoption-X) 命令行选项。 （由 Yilei Yang 在 [gh-111374](https://github.com/python/cpython/issues/111374) 中贡献。）
   
*   通过新的环境变量 [`PYTHON_PERF_JIT_SUPPORT`](../using/cmdline.html#envvar-PYTHON_PERF_JIT_SUPPORT) 和命令行选项 [`-X perf_jit`](../using/cmdline.html#cmdoption-X) 添加无需 [帧指针](https://en.wikipedia.org/wiki/Call_stack) 即可工作的 [对 perf 性能分析器的支持](../howto/perf_profiling.html#perf-profiling)。 （由 Pablo Galindo 在 [gh-118518](https://github.com/python/cpython/issues/118518) 中贡献。）
   
*   可通过新的 [`PYTHON_HISTORY`](../using/cmdline.html#envvar-PYTHON_HISTORY) 环境变量来更改 `.python_history` 文件的位置。 （由 Levi Sabah, Zackery Spytz 和 Hugo van Kemenade 在 [gh-73965](https://github.com/python/cpython/issues/73965) 中贡献。）
   
*   类新增了一个 [`__static_attributes__`](../reference/datamodel.html#type.__static_attributes__ "type.__static_attributes__") 属性。 这由编译器以类属性名称的元组来填充，这些名称是从类体中的任何函数通过 `self.<name>` 来赋值的。 （由 Irit Katriel 在 [gh-115775](https://github.com/python/cpython/issues/115775) 中贡献。）.)
   
*   编译器现在会在类上创建一个 `__firstlineno__` 属性，其值为类定义第一行的行号。 （由 Serhiy Storchaka 在 [gh-118465](https://github.com/python/cpython/issues/118465) 中贡献。）
   
*   现在 [`exec()`](../library/functions.html#exec "exec") 和 [`eval()`](../library/functions.html#eval "eval") 内置函数接受以关键字形式传入的 _globals_ 和 _locals_ 参数。 （由 Raphael Gaschignard 在 [gh-105879](https://github.com/python/cpython/issues/105879) 中贡献。）
   
*   现在 [`compile()`](../library/functions.html#compile "compile") 内置函数接受一个新的旗标 `ast.PyCF_OPTIMIZED_AST`，它类似于 `ast.PyCF_ONLY_AST` 但区别在于返回的 AST 是根据 _optimize_ 参数的值进行优化的。 （由 Irit Katriel 在 [gh-108113](https://github.com/python/cpython/issues/108113) 中贡献。）
   
*   在 [`property`](../library/functions.html#property "property") 对象上增加了 [`__name__`](../library/functions.html#property.__name__ "property.__name__") 属性。 （由 Eugene Toder 在 [gh-101860](https://github.com/python/cpython/issues/101860) 中贡献。）
   
*   增加了新的异常 [`PythonFinalizationError`](../library/exceptions.html#PythonFinalizationError "PythonFinalizationError")，它派生自 [`RuntimeError`](../library/exceptions.html#RuntimeError "RuntimeError")，用于当操作在 [最终化](../glossary.html#term-interpreter-shutdown) 期间被阻塞时发出信号。 下列可调用对象现在将引发 `PythonFinalizationError`，而不是 [`RuntimeError`](../library/exceptions.html#RuntimeError "RuntimeError"):
   
   *   [`_thread.start_new_thread()`](../library/_thread.html#thread.start_new_thread "_thread.start_new_thread")
       
   *   [`os.fork()`](../library/os.html#os.fork "os.fork")
       
   *   [`os.forkpty()`](../library/os.html#os.forkpty "os.forkpty")
       
   *   [`subprocess.Popen`](../library/subprocess.html#subprocess.Popen "subprocess.Popen")
       
   
   （由 Victor Stinner 在 [gh-114570](https://github.com/python/cpython/issues/114570) 中贡献。）
   
*   允许 [`str.replace()`](../library/stdtypes.html#str.replace "str.replace") 的 _count_ 参数为关键字参数。 （由 Hugo van Kemenade 在 [gh-106487](https://github.com/python/cpython/issues/106487) 中贡献。）
   
*   现在许多函数会对将布尔值作为文件描述符参数发出警告。这可以帮助尽早发现一些错误。（由 Serhiy Storchaka 在 [gh-82626](https://github.com/python/cpython/issues/82626) 中贡献。）
   
*   为 [`bz2`](../library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression."), [`lzma`](../library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library."), [`tarfile`](../library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.") 和 [`zipfile`](../library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") 等模块中的已压缩和已归档文件型对象添加了 `name` 和 `mode` 属性。 （由 Serhiy Storchaka 在 [gh-115961](https://github.com/python/cpython/issues/115961) 中贡献。）
   

新增模块[¶](#new-modules "Link to this heading")
--------------------------------------------

*   [`dbm.sqlite3`](../library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm (All)"): 针对 [`dbm`](../library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats.") 的 SQLite 后端。 （由 Raymond Hettinger 和 Erlend E. Aasland 在 [gh-100414](https://github.com/python/cpython/issues/100414) 中贡献。）
   

改进的模块[¶](#improved-modules "Link to this heading")
--------------------------------------------------

### argparse[¶](#argparse "Link to this heading")

*   为 [`add_argument()`](../library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") 和 `add_parser()` 方法添加了 _deprecated_ 形参，以允许弃用命令行选项、位置参数和子命令。 （由 Serhiy Storchaka 在 [gh-83648](https://github.com/python/cpython/issues/83648) 中贡献。）
   

### array[¶](#array "Link to this heading")

*   增加了 `'w'` 类型码 (`Py_UCS4`) 表示 Unicode 字符。 它应被用来代替已弃用的 `'u'` 类型码。 （由 Inada Naoki 在 [gh-80480](https://github.com/python/cpython/issues/80480) 中贡献。）
   
*   通过实现 [`clear()`](../library/array.html#array.array.clear "array.array.clear") 方法将 [`array.array`](../library/array.html#array.array "array.array") 注册为 [`MutableSequence`](../library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence")。 （由 Mike Zimin 在 [gh-114894](https://github.com/python/cpython/issues/114894) 中贡献。）
   

### ast[¶](#ast "Link to this heading")

*   现在 [`ast`](../library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") 模块中节点类型的构造器对其接受的参数要求更为严格，并在参数被省略时有更易理解的行为。
   
   如果在构造实例时某个 AST 节点上的可选字段没有被作为参数包括在内，则该字段现在将被设为 `None`。 类似地，如果某个列表字段被省略，则该字段现在将被设为空列表，而如果某个 `expr_context` 字段被省略，则它将默认为 [`Load()`](../library/ast.html#ast.Load "ast.Load")。 （之前，在所有情况下，新构造的 AST 节点实例上的相应属性都将缺失。）
   
   在所有其他情况下，当需要的参数被省略时，节点构造器将发出 [`DeprecationWarning`](../library/exceptions.html#DeprecationWarning "DeprecationWarning")。 这在 Python 3.15 中将会引发异常。 类似地，将关键字参数传入一个未映射到 AST 节点上的字段的构造器的做法现在已被弃用，并且在 Python 3.15 中将会引发异常。
   
   这些更改将不会应用于用户自定义的 [`ast.AST`](../library/ast.html#ast.AST "ast.AST") 子类，除非该类选择通过设置 [`AST._field_types`](../library/ast.html#ast.AST._field_types "ast.AST._field_types") 映射的方式加入新的行为。
   
   （由 Jelle Zijlstra 在 [gh-105858](https://github.com/python/cpython/issues/105858), [gh-117486](https://github.com/python/cpython/issues/117486) 和 [gh-118851](https://github.com/python/cpython/issues/118851) 中贡献。）
   
*   现在 [`ast.parse()`](../library/ast.html#ast.parse "ast.parse") 接受一个可选参数 _optimize_，它会被传递给 [`compile()`](../library/functions.html#compile "compile")。 这使得获取已优化的 AST 成为可能。 （由 Irit Katriel 在 [gh-108113](https://github.com/python/cpython/issues/108113) 中贡献。）
   

### asyncio[¶](#asyncio "Link to this heading")

*   现在 [`asyncio.as_completed()`](../library/asyncio-task.html#asyncio.as_completed "asyncio.as_completed") 将返回一个即是 [asynchronous iterator](../glossary.html#term-asynchronous-iterator) 又是基本的产生 [可等待对象](../glossary.html#term-awaitable) 的 [iterator](../glossary.html#term-iterator) 的对象。 由异常迭代产生的可等待对象包括被传入的原始 Task 或 Future 对象，使得将结果与正在完成的任务相关联更为容易。 （由 Justin Arthur 在 [gh-77714](https://github.com/python/cpython/issues/77714) 中贡献。）
   
*   现在当服务器被关闭时 [`asyncio.loop.create_unix_server()`](../library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server") 会自动移除 Unix 套接字。 （由 Pierre Ossman 在 [gh-111246](https://github.com/python/cpython/issues/111246) 中贡献。）
   
*   现在当附带一个空字节串对象调用时 [`DatagramTransport.sendto()`](../library/asyncio-protocol.html#asyncio.DatagramTransport.sendto "asyncio.DatagramTransport.sendto") 将发送零长度的数据报。 现在当计算缓冲区大小时传输控制流还会将数据报标头纳入考量。 （由 Jamie Phan 在 [gh-115199](https://github.com/python/cpython/issues/115199) 中贡献。）
   
*   增加了 [`Queue.shutdown`](../library/asyncio-queue.html#asyncio.Queue.shutdown "asyncio.Queue.shutdown") 和 [`QueueShutDown`](../library/asyncio-queue.html#asyncio.QueueShutDown "asyncio.QueueShutDown") 用于管理队列终结。 （由 Laurie Opperman 和 Yves Duprat 在 [gh-104228](https://github.com/python/cpython/issues/104228) 中贡献。）
   
*   增加了 [`Server.close_clients()`](../library/asyncio-eventloop.html#asyncio.Server.close_clients "asyncio.Server.close_clients") 和 [`Server.abort_clients()`](../library/asyncio-eventloop.html#asyncio.Server.abort_clients "asyncio.Server.abort_clients") 方法，它们会以更强制的方式关闭 asyncio 服务器。 （由 Pierre Ossman 在 [gh-113538](https://github.com/python/cpython/issues/113538) 中贡献。）
   
*   在 [`StreamReader.readuntil()`](../library/asyncio-stream.html#asyncio.StreamReader.readuntil "asyncio.StreamReader.readuntil") 中接受一个由分隔符组成的元组，当遇到其中之一时就会停止。 （由 Bruce Merry 在 [gh-81322](https://github.com/python/cpython/issues/81322) 中贡献。）
   
*   改进了 [`TaskGroup`](../library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup") 在外部的取消操作与内部的取消操作发生冲突时的行为。 例如，当嵌套两个任务分组并且两者同时在某个子任务中遇到异常时，外层的任务分组有可能被挂起，因为其内部的取消操作已由内层的任务分组进行处理。
   
   对于任务分组在外部被取消时同时必须引发 [`ExceptionGroup`](../library/exceptions.html#ExceptionGroup "ExceptionGroup") 的情况，现在它将调用父任务的 [`cancel()`](../library/asyncio-task.html#asyncio.Task.cancel "asyncio.Task.cancel") 方法。 这样可以确保 [`CancelledError`](../library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") 会在下一次 [`await`](../reference/expressions.html#await) 时被引发，因此取消操作不会丢失。, so the cancellation is not lost.
   
   这些更改的一个附加好处是现在任务组会保留取消操作计数 ([`cancelling()`](../library/asyncio-task.html#asyncio.Task.cancelling "asyncio.Task.cancelling"))。
   
   为了处理某些边界情况，现在 [`uncancel()`](../library/asyncio-task.html#asyncio.Task.uncancel "asyncio.Task.uncancel") 可以在取消操作计数达到零时重置未写入文档的 `_must_cancel` 旗标。
   
   （受到由 Arthur Tacca 在 [gh-116720](https://github.com/python/cpython/issues/116720) 中报告的问题的启发。）
   
*   当在一个未激活的 [`TaskGroup`](../library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup") 上调用 [`TaskGroup.create_task()`](../library/asyncio-task.html#asyncio.TaskGroup.create_task "asyncio.TaskGroup.create_task") 时，给定的协程将被关闭 (这将防止引发有关给定的协程从未被等待的 [`RuntimeWarning`](../library/exceptions.html#RuntimeWarning "RuntimeWarning"))。 （由 Arthur Tacca 和 Jason Zhang 在 [gh-115957](https://github.com/python/cpython/issues/115957) 中贡献。）
   

### base64[¶](#base64 "Link to this heading")

*   增加了 [`z85encode()`](../library/base64.html#base64.z85encode "base64.z85encode") 和 [`z85decode()`](../library/base64.html#base64.z85decode "base64.z85decode") 函数用于将 [`bytes`](../library/stdtypes.html#bytes "bytes") 编码为 [Z85 data](https://rfc.zeromq.org/spec/32/) 和将 Z85 编码的数据解码为 `bytes`。 （由 Matan Perelman 在 [gh-75299](https://github.com/python/cpython/issues/75299) 中贡献。）
   

### compileall[¶](#compileall "Link to this heading")

*   工作线程和进程的默认数据现在是使用 [`os.process_cpu_count()`](../library/os.html#os.process_cpu_count "os.process_cpu_count") 而不是 [`os.cpu_count()`](../library/os.html#os.cpu_count "os.cpu_count") 来选择的。 （由 Victor Stinner 在 [gh-109649](https://github.com/python/cpython/issues/109649) 中贡献。）
   

### concurrent.futures[¶](#concurrent-futures "Link to this heading")

*   工作线程和进程的默认数据现在是使用 [`os.process_cpu_count()`](../library/os.html#os.process_cpu_count "os.process_cpu_count") 而不是 [`os.cpu_count()`](../library/os.html#os.cpu_count "os.cpu_count") 来选择的。 （由 Victor Stinner 在 [gh-109649](https://github.com/python/cpython/issues/109649) 中贡献。）
   

### configparser[¶](#configparser "Link to this heading")

*   现在 [`ConfigParser`](../library/configparser.html#configparser.ConfigParser "configparser.ConfigParser") 具有对未命名节的支持，这将允许使用最高层级的键值对。 此特性可通过新增的 _allow\_unnamed\_section_ 形参来启用。 （由 Pedro Sousa Lacerda 在 [gh-66449](https://github.com/python/cpython/issues/66449) 中贡献。）
   

### copy[¶](#copy "Link to this heading")

*   新增的 [`replace()`](../library/copy.html#copy.replace "copy.replace") 函数和 [`replace 协议`](../library/copy.html#object.__replace__ "object.__replace__") 使得创建经修改的对象副本更为简单。 这在操作不可变对象时特别有用。 以下类型将支持 [`replace()`](../library/copy.html#copy.replace "copy.replace") 函数并实现了 replace 协议：
   
   *   [`collections.namedtuple()`](../library/collections.html#collections.namedtuple "collections.namedtuple")
       
   *   [`dataclasses.dataclass`](../library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass")
       
   *   [`datetime.datetime`](../library/datetime.html#datetime.datetime "datetime.datetime"), [`datetime.date`](../library/datetime.html#datetime.date "datetime.date"), [`datetime.time`](../library/datetime.html#datetime.time "datetime.time")
       
   *   [`inspect.Signature`](../library/inspect.html#inspect.Signature "inspect.Signature"), [`inspect.Parameter`](../library/inspect.html#inspect.Parameter "inspect.Parameter")
       
   *   [`types.SimpleNamespace`](../library/types.html#types.SimpleNamespace "types.SimpleNamespace")
       
   *   [代码对象](../reference/datamodel.html#code-objects)
       
   
   任何用户自定义类也可以通过定义 [`__replace__()`](../library/copy.html#object.__replace__ "object.__replace__") 方法来支持 [`copy.replace()`](../library/copy.html#copy.replace "copy.replace")。 （由 Serhiy Storchaka 在 [gh-108751](https://github.com/python/cpython/issues/108751) 中贡献。）
   

### ctypes[¶](#ctypes "Link to this heading")

*   作为必要的内部重构的一个后果，内部元类的初始化现在将发生于 `__init__` 中而不是 `__new__` 中。 这会影响子类化这些内部元类以提供自定义初始化的项目。 一般而言：
   
   *   调用 `super().__new__` 之后在 `__new__` 中完成的自定义逻辑应当移至 `__init__`。
       
   *   要创建一个类，需调用相应的元类，而不仅是该元类的 `__new__` 方法。
       
   
   请参阅 [gh-124520](https://github.com/python/cpython/issues/124520) 了解相关讨论和对某些受影响项目的修改的链接。
   
*   [`ctypes.Structure`](../library/ctypes.html#ctypes.Structure "ctypes.Structure") objects have a new [`_align_`](../library/ctypes.html#ctypes.Structure._align_ "ctypes.Structure._align_") attribute which allows the alignment of the structure being packed to/from memory to be specified explicitly. (Contributed by Matt Sanderson in [gh-112433](https://github.com/python/cpython/issues/112433))
   

### dbm[¶](#dbm "Link to this heading")

*   增加 [`dbm.sqlite3`](../library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm (All)")，一个实现了 SQLite 后端的新模块，并将其设为默认的 `dbm` 后端。 （由 Raymond Hettinger 和 Erlend E. Aasland 在 [gh-100414](https://github.com/python/cpython/issues/100414) 中贡献。）
   
*   允许通过新增的 [`gdbm.clear()`](../library/dbm.html#dbm.gnu.gdbm.clear "dbm.gnu.gdbm.clear") 和 [`ndbm.clear()`](../library/dbm.html#dbm.ndbm.ndbm.clear "dbm.ndbm.ndbm.clear") 方法移除数据库中的所有条目。 （由 Donghee Na 在 [gh-107122](https://github.com/python/cpython/issues/107122) 中贡献。）
   

### dis[¶](#dis "Link to this heading")

*   将 [`dis`](../library/dis.html#module-dis "dis: Disassembler for Python bytecode.") 模块的函数的输出修改为显示跳转目标和异常处理器的逻辑标签，而不是偏移量。 可以使用新的 [`-O`](../library/dis.html#cmdoption-dis-O) 命令行选项或 _show\_offsets_ 参数来添加偏移量。 （由 Irit Katriel 在 [gh-112137](https://github.com/python/cpython/issues/112137) 中贡献。）
   
*   [`get_instructions()`](../library/dis.html#dis.get_instructions "dis.get_instructions") 不再将缓存条目表示为单独的指令。 作为替代，它会将它们作为 [`Instruction`](../library/dis.html#dis.Instruction "dis.Instruction") 的组成部分返回，放在新的 _cache\_info_ 字段中。 传给 [`get_instructions()`](../library/dis.html#dis.get_instructions "dis.get_instructions") 的 _show\_caches_ 参数已被弃用并且不再有任何效果。 （由 Irit Katriel 在 [gh-112962](https://github.com/python/cpython/issues/112962) 中贡献。）
   

### doctest[¶](#doctest "Link to this heading")

*   现在 [`doctest`](../library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") 输出默认是彩色的。 此特性可通过新增的 [`PYTHON_COLORS`](../using/cmdline.html#envvar-PYTHON_COLORS) 环境变量和传统的 [`NO_COLOR`](https://no-color.org/) 和 [`FORCE_COLOR`](https://force-color.org/) 环境变量来控制。 另请参阅 [控制颜色](../using/cmdline.html#using-on-controlling-color)。 （由 Hugo van Kemenade 在 [gh-117225](https://github.com/python/cpython/issues/117225) 中贡献。）
   
*   现在 [`DocTestRunner.run()`](../library/doctest.html#doctest.DocTestRunner.run "doctest.DocTestRunner.run") 方法会统计已跳过测试的数量。 增加了 [`DocTestRunner.skips`](../library/doctest.html#doctest.DocTestRunner.skips "doctest.DocTestRunner.skips") 和 [`TestResults.skipped`](../library/doctest.html#doctest.TestResults.skipped "doctest.TestResults.skipped") 属性。 （由 Victor Stinner 在 [gh-108794](https://github.com/python/cpython/issues/108794) 中贡献。）
   

### email[¶](#email "Link to this heading")

*   现在带有嵌入的换行符的标头在输出时会加上引号。 现在 [`generator`](../library/email.generator.html#module-email.generator "email.generator: Generate flat text email messages from a message structure.") 会拒绝序列化（写入）不正确地折叠或分隔的标头，例如将被解析为多个标头或与相邻数据合并的标头等。 如果你需要禁用此安全特性，请设置 [`verify_generated_headers`](../library/email.policy.html#email.policy.Policy.verify_generated_headers "email.policy.Policy.verify_generated_headers")。 （由 Bas Bloemsaat 和 Petr Viktorin 在 [gh-121650](https://github.com/python/cpython/issues/121650) 中贡献。）
   
*   现在 [`getaddresses()`](../library/email.utils.html#email.utils.getaddresses "email.utils.getaddresses") 和 [`parseaddr()`](../library/email.utils.html#email.utils.parseaddr "email.utils.parseaddr") 会在更多遇到无效 email 地址的情况下返回 `('', '')` 对非可能不准确的值。 这两个函数新增了可选的 _strict_ 形参 (默认为 `True`)。 要获取旧版本的行为 (接受错误格式的输入)，请使用 `strict=False`。 `getattr(email.utils, 'supports_strict_parsing', False)` 可被用于检查 _strict_ 形参是否可用。 （由 Thomas Dwyer 和 Victor Stinner 针对 [gh-102988](https://github.com/python/cpython/issues/102988) 贡献以改进 [**CVE 2023-27043**](https://www.cve.org/CVERecord?id=CVE-2023-27043) 修正。）
   

### fractions[¶](#fractions "Link to this heading")

*   现在 [`Fraction`](../library/fractions.html#fractions.Fraction "fractions.Fraction") 对象支持用于填充、对齐、正负号处理、最小宽度和分组的标准 [格式说明迷你语言](../library/string.html#formatspec) 规则。 （由 Mark Dickinson 在 [gh-111320](https://github.com/python/cpython/issues/111320) 中贡献。）
   

### glob[¶](#glob "Link to this heading")

*   增加了 [`translate()`](../library/glob.html#glob.translate "glob.translate")，这是个用来将具有 shell 风格通配符的路径说明转换为正则表达式的函数。 （由 Barney Gale 在 [gh-72904](https://github.com/python/cpython/issues/72904) 中贡献。）
   

### importlib[¶](#importlib "Link to this heading")

*   现在 [`importlib.resources`](../library/importlib.resources.html#module-importlib.resources "importlib.resources: Package resource reading, opening, and access") 中的下列函数允许访问资源目录（或树），并使用多个位置参数（现在文本读取函数中的 _encoding_ 和 _errors_ 参数是仅限关键字参数）：
   
   *   [`is_resource()`](../library/importlib.resources.html#importlib.resources.is_resource "importlib.resources.is_resource")
       
   *   [`open_binary()`](../library/importlib.resources.html#importlib.resources.open_binary "importlib.resources.open_binary")
       
   *   [`open_text()`](../library/importlib.resources.html#importlib.resources.open_text "importlib.resources.open_text")
       
   *   [`path()`](../library/importlib.resources.html#importlib.resources.path "importlib.resources.path")
       
   *   [`read_binary()`](../library/importlib.resources.html#importlib.resources.read_binary "importlib.resources.read_binary")
       
   *   [`read_text()`](../library/importlib.resources.html#importlib.resources.read_text "importlib.resources.read_text")
       
   
   These functions are no longer deprecated and are not scheduled for removal. (Contributed by Petr Viktorin in [gh-116608](https://github.com/python/cpython/issues/116608).)
   
*   [`contents()`](../library/importlib.resources.html#importlib.resources.contents "importlib.resources.contents") remains deprecated in favor of the fully-featured [`Traversable`](../library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable") API. However, there is now no plan to remove it. (Contributed by Petr Viktorin in [gh-116608](https://github.com/python/cpython/issues/116608).)
   

### io[¶](#io "Link to this heading")

*   现在 [`IOBase`](../library/io.html#io.IOBase "io.IOBase") 最终化器会使用 [`sys.unraisablehook`](../library/sys.html#sys.unraisablehook "sys.unraisablehook") 来将由 [`close()`](../library/io.html#io.IOBase.close "io.IOBase.close") 方法引发的错误写入日志。 在之前版本中，错误在默认情况下会被静默地忽略，而只有在 [Python 开发模式](../library/devmode.html#devmode) 或在使用 [Python 调试构建版](../using/configure.html#debug-build) 时才会被写入日志。 （由 Victor Stinner 在 [gh-62948](https://github.com/python/cpython/issues/62948) 中贡献。）
   

### ipaddress[¶](#ipaddress "Link to this heading")

*   增加了 [`IPv4Address.ipv6_mapped`](../library/ipaddress.html#ipaddress.IPv4Address.ipv6_mapped "ipaddress.IPv4Address.ipv6_mapped") 特征属性，它将返回映射 IPv4 的 IPv6 地址。 （由 Charles Machalow 在 [gh-109466](https://github.com/python/cpython/issues/109466) 中贡献。）
   
*   修正了 [`IPv4Address`](../library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address"), [`IPv6Address`](../library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address"), [`IPv4Network`](../library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network") 和 [`IPv6Network`](../library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network") 中 `is_global` 和 `is_private` 的行为。 （由 Jakub Stasiak 在 [gh-113171](https://github.com/python/cpython/issues/113171) 中贡献。）
   

### itertools[¶](#itertools "Link to this heading")

*   [`batched()`](../library/itertools.html#itertools.batched "itertools.batched") 新增了 _strict_ 形参，它会在最后一批次数据小于指定批准大小时引发 [`ValueError`](../library/exceptions.html#ValueError "ValueError")。 （由 Raymond Hettinger 在 [gh-113202](https://github.com/python/cpython/issues/113202) 中贡献。）
   

### marshal[¶](#marshal "Link to this heading")

*   在模块函数中增加了 _allow\_code_ 形参。 传入 `allow_code=False` 将防止在 Python 各版本间不兼容的代码对象的序列化和反序列化。 （由 Serhiy Storchaka 在 [gh-113626](https://github.com/python/cpython/issues/113626) 中贡献。）
   

### math[¶](#math "Link to this heading")

*   新增函数 [`fma()`](../library/math.html#math.fma "math.fma") 可执行合并的乘法-加法运算。 此函数只需一轮操作即可计算 `x * y + z`，从而避免了任何中间步骤导致的精度损失。 它包装了 C99 所提供的 `fma()` 函数，并且遵从针对特殊情况的 IEEE 754 "fusedMultiplyAdd" 运算规范。 （由 Mark Dickinson 和 Victor Stinner 在 [gh-73468](https://github.com/python/cpython/issues/73468) 中贡献。）
   

### mimetypes[¶](#mimetypes "Link to this heading")

*   增加了 [`guess_file_type()`](../library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type") 函数用于根据文件系统路径来猜测 MIME 类型。 在 [`guess_type()`](../library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") 中使用路径的做法现在已是 [soft deprecated](../glossary.html#term-soft-deprecated)。 （由 Serhiy Storchaka 在 [gh-66543](https://github.com/python/cpython/issues/66543) 中贡献。）
   

### mmap[¶](#mmap "Link to this heading")

*   现在 [`mmap`](../library/mmap.html#mmap.mmap "mmap.mmap") 在 Windows 上当被映射的内存由于文件系统错误或访问限制而不可访问时将获得保护以避免崩溃。 （由 Jannis Weigend 在 [gh-118209](https://github.com/python/cpython/issues/118209) 中贡献。）
   
*   [`mmap`](../library/mmap.html#mmap.mmap "mmap.mmap") 具有新的 [`seekable()`](../library/mmap.html#mmap.mmap.seekable "mmap.mmap.seekable") 方法将在需要可定位的文件型对象时被使用。 现在 [`seek()`](../library/mmap.html#mmap.mmap.seek "mmap.mmap.seek") 方法将返回一个新的绝对位置。 （由 Donghee Na 和 Sylvie Liberman 在 [gh-111835](https://github.com/python/cpython/issues/111835) 中贡献。）
   
*   [`mmap`](../library/mmap.html#mmap.mmap "mmap.mmap") 新增了 UNIX 专属的 _trackfd_ 形参用来控制文件描述符的复制；如为假值，则由 _fileno_ 指定的文件描述符将不会被复制。 （由 Zackery Spytz 和 Petr Viktorin 在 [gh-78502](https://github.com/python/cpython/issues/78502) 中贡献。）
   

### multiprocessing[¶](#multiprocessing "Link to this heading")

*   工作线程和进程的默认数据现在是使用 [`os.process_cpu_count()`](../library/os.html#os.process_cpu_count "os.process_cpu_count") 而不是 [`os.cpu_count()`](../library/os.html#os.cpu_count "os.cpu_count") 来选择的。 （由 Victor Stinner 在 [gh-109649](https://github.com/python/cpython/issues/109649) 中贡献。）
   

### os[¶](#os "Link to this heading")

*   增加了 [`process_cpu_count()`](../library/os.html#os.process_cpu_count "os.process_cpu_count") 函数用于获取当前进程的调用方线程可以使用的逻辑 CPU 核心数量。 （由 Victor Stinner 在 [gh-109649](https://github.com/python/cpython/issues/109649) 中贡献。）
   
*   [`cpu_count()`](../library/os.html#os.cpu_count "os.cpu_count") 和 [`process_cpu_count()`](../library/os.html#os.process_cpu_count "os.process_cpu_count") 可通过新的环境变量 [`PYTHON_CPU_COUNT`](../using/cmdline.html#envvar-PYTHON_CPU_COUNT) 或新的命令行选项 [`-X cpu_count`](../using/cmdline.html#cmdoption-X) 来覆盖。 此选项对于需要在不修改应用程序代码或容器本身的情况下限制一个容器系统的 CPU 资源的用户会很有用处。 （由 Donghee Na 在 [gh-109595](https://github.com/python/cpython/issues/109595) 中贡献。）
   
*   通过 [`timerfd_create()`](../library/os.html#os.timerfd_create "os.timerfd_create"), [`timerfd_settime()`](../library/os.html#os.timerfd_settime "os.timerfd_settime"), [`timerfd_settime_ns()`](../library/os.html#os.timerfd_settime_ns "os.timerfd_settime_ns"), [`timerfd_gettime()`](../library/os.html#os.timerfd_gettime "os.timerfd_gettime"), [`timerfd_gettime_ns()`](../library/os.html#os.timerfd_gettime_ns "os.timerfd_gettime_ns"), [`TFD_NONBLOCK`](../library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK"), [`TFD_CLOEXEC`](../library/os.html#os.TFD_CLOEXEC "os.TFD_CLOEXEC"), [`TFD_TIMER_ABSTIME`](../library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME") 和 [`TFD_TIMER_CANCEL_ON_SET`](../library/os.html#os.TFD_TIMER_CANCEL_ON_SET "os.TFD_TIMER_CANCEL_ON_SET") 增加了针对 Linux 的 _[计算器文件描述符](https://manpages.debian.org/timerfd_create(2))_ 的 [低层级接口](../library/os.html#os-timerfd)。 （由 Masaru Tsuchiyama 在 [gh-108277](https://github.com/python/cpython/issues/108277) 中贡献。）
   
*   在 Windows 上现在同时增加了对 [`lchmod()`](../library/os.html#os.lchmod "os.lchmod") 和 [`chmod()`](../library/os.html#os.chmod "os.chmod") 的 _follow\_symlinks_ 参数的支持。 请注意在 Windows 上 `lchmod()` 中的 _follow\_symlinks_ 的默认值为 `False`。 （由 Serhiy Storchaka 在 [gh-59616](https://github.com/python/cpython/issues/59616) 中贡献。）
   
*   在 Windows 上现在同时增加了 [`fchmod()`](../library/os.html#os.fchmod "os.fchmod") 和对 [`chmod()`](../library/os.html#os.chmod "os.chmod") 中的文件描述符的支持。 （由 Serhiy Storchaka 在 [gh-113191](https://github.com/python/cpython/issues/113191) 中贡献。）
   
*   在 Windows 上，[`mkdir()`](../library/os.html#os.mkdir "os.mkdir") 和 [`makedirs()`](../library/os.html#os.makedirs "os.makedirs") 现在支持传入 _mode_ 值 `0o700` 以对新目录应用访问控制。 这会隐式地影响 [`tempfile.mkdtemp()`](../library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp") 并可缓解 [**CVE 2024-4030**](https://www.cve.org/CVERecord?id=CVE-2024-4030)。 其他的 _mode_ 值仍然会被忽略。 （由 Steve Dower 在 [gh-118486](https://github.com/python/cpython/issues/118486) 中贡献。）
   
*   现在 [`posix_spawn()`](../library/os.html#os.posix_spawn "os.posix_spawn") 可接受 `None` 作为 _env_ 参数，这将让新产生的进程使用当前进程的环境。 （由 Jakub Kulik 在 [gh-113119](https://github.com/python/cpython/issues/113119) 中贡献。）.)
   
*   在支持 `posix_spawn_file_actions_addclosefrom_np()` 的平台上 [`posix_spawn()`](../library/os.html#os.posix_spawn "os.posix_spawn") 现在可以在 _file\_actions_ 形参中使用 [`POSIX_SPAWN_CLOSEFROM`](../library/os.html#os.POSIX_SPAWN_CLOSEFROM "os.POSIX_SPAWN_CLOSEFROM") 属性。 （由 Jakub Kulik 在 [gh-113117](https://github.com/python/cpython/issues/113117) 中贡献。）.)
   

### os.path[¶](#os-path "Link to this heading")

*   增加了 [`isreserved()`](../library/os.path.html#os.path.isreserved "os.path.isreserved") 用于检查一个路径在当前系统中是否为保留路径。 此函数仅在 Windows 上可用。 （由 Barney Gale 在 [gh-88569](https://github.com/python/cpython/issues/88569) 中贡献。）
   
*   在 Windows 上，[`isabs()`](../library/os.path.html#os.path.isabs "os.path.isabs") 将不再把以恰好一个斜杠 (`\` 或 `/`) 开头的路径视为绝对路径。 （由 Barney Gale 和 Jon Foster 在 [gh-44626](https://github.com/python/cpython/issues/44626) 中贡献。）
   
*   现在即使文件不可访问 [`realpath()`](../library/os.path.html#os.path.realpath "os.path.realpath") 也能够解析 MS-DOS 风格的文件名。 （由 Moonsik Park 在 [gh-82367](https://github.com/python/cpython/issues/82367) 中贡献。）
   

### pathlib[¶](#pathlib "Link to this heading")

*   增加了 [`UnsupportedOperation`](../library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation")，它会在一个路径操作不受支持时代替 [`NotImplementedError`](../library/exceptions.html#NotImplementedError "NotImplementedError") 被引发。 （由 Barney Gale 在 [gh-89812](https://github.com/python/cpython/issues/89812) 中贡献。）
   
*   新增了一个用于根据 'file' URI (`file:///`) 来创建 [`Path`](../library/pathlib.html#pathlib.Path "pathlib.Path") 对象的构造器 [`Path.from_uri()`](../library/pathlib.html#pathlib.Path.from_uri "pathlib.Path.from_uri")。 （由 Barney Gale 在 [gh-107465](https://github.com/python/cpython/issues/107465) 中贡献。）
   
*   增加了 [`PurePath.full_match()`](../library/pathlib.html#pathlib.PurePath.full_match "pathlib.PurePath.full_match") 用于匹配带有 shell 风格通配符的路径，包括递归通配符 "`**`"。 （由 Barney Gale 在 [gh-73435](https://github.com/python/cpython/issues/73435) 中贡献。）
   
*   增加了 [`PurePath.parser`](../library/pathlib.html#pathlib.PurePath.parser "pathlib.PurePath.parser") 类属性以存储用于低层级路径解析与合并的 [`os.path`](../library/os.path.html#module-os.path "os.path: Operations on pathnames.") 实现。 这可以是 `posixpath` 或 `ntpath`。
   
*   为 [`Path.glob()`](../library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob") 和 [`rglob()`](../library/pathlib.html#pathlib.Path.rglob "pathlib.Path.rglob") 增加了 _recurse\_symlinks_ 仅限关键字参数。 （由 Barney Gale 在 [gh-77609](https://github.com/python/cpython/issues/77609) 中贡献。）
   
*   现在当给出以 "`**`" 结束的模式时 [`Path.glob()`](../library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob") 和 [`rglob()`](../library/pathlib.html#pathlib.Path.rglob "pathlib.Path.rglob") 将返回文件和目录。 在之前版本中，仅会返回目录。 （由 Barney Gale 在 [gh-70303](https://github.com/python/cpython/issues/70303) 中贡献。）.)
   
*   为 [`Path.is_file`](../library/pathlib.html#pathlib.Path.is_file "pathlib.Path.is_file"), [`Path.is_dir`](../library/pathlib.html#pathlib.Path.is_dir "pathlib.Path.is_dir"), [`Path.owner()`](../library/pathlib.html#pathlib.Path.owner "pathlib.Path.owner") 和 [`Path.group()`](../library/pathlib.html#pathlib.Path.group "pathlib.Path.group") 增加了 _follow\_symlinks_ 仅限关键字参数。 （由 Barney Gale 在 [gh-105793](https://github.com/python/cpython/issues/105793) 中，以及 Kamil Turek 在 [gh-107962](https://github.com/python/cpython/issues/107962) 中贡献。）
   

### pdb[¶](#pdb "Link to this heading")

*   现在 [`breakpoint()`](../library/functions.html#breakpoint "breakpoint") 和 [`set_trace()`](../library/pdb.html#pdb.set_trace "pdb.set_trace") 会立即进入调试器而不是在被执行代码的下一行进入。 这一更改可防止当 `breakpoint()` 位于上下文末尾 时调试器在上下文以外被中断。 （由 Tian Gao 在 [gh-118579](https://github.com/python/cpython/issues/118579) 中贡献。）
   
*   当设置了 [`sys.flags.safe_path`](../library/sys.html#sys.flags.safe_path "sys.flags.safe_path") 时 `sys.path[0]` 将不会再被替换为被调试脚本的目录。 （由 Tian Gao 和 Christian Walther 在 [gh-111762](https://github.com/python/cpython/issues/111762) 中贡献。）
   
*   现在支持将 [`zipapp`](../library/zipapp.html#module-zipapp "zipapp: Manage executable Python zip archives") 作为调试目标。 （由 Tian Gao 在 [gh-118501](https://github.com/python/cpython/issues/118501) 中贡献。）
   
*   添加了在 [`pm()`](../library/pdb.html#pdb.pm "pdb.pm") 中进行事后调试期间使用 Pdb 新增的 [`exceptions [exc_number]`](../library/pdb.html#pdbcommand-exceptions) 命令在串连的异常之间移动的能力。 （由 Matthias Bussonnier 在 [gh-106676](https://github.com/python/cpython/issues/106676) 中贡献。）
   
*   以一条 pdb 命令打头的表达式和语句现在会被正确地标识并执行。 （由 Tian Gao 在 [gh-108464](https://github.com/python/cpython/issues/108464) 中贡献。）
   

### queue[¶](#queue "Link to this heading")

*   增加了 [`Queue.shutdown`](../library/queue.html#queue.Queue.shutdown "queue.Queue.shutdown") 和 [`ShutDown`](../library/queue.html#queue.ShutDown "queue.ShutDown") 用于管理队列的终结。 （由 Laurie Opperman 和 Yves Duprat 在 [gh-104750](https://github.com/python/cpython/issues/104750) 中贡献。）
   

### random[¶](#random "Link to this heading")

*   增加了一个 [命令行接口](../library/random.html#random-cli)。 （由 Hugo van Kemenade 在 [gh-118131](https://github.com/python/cpython/issues/118131) 中贡献。）
   

### re[¶](#re "Link to this heading")

*   将 `re.error` 重命名为 [`PatternError`](../library/re.html#re.PatternError "re.PatternError") 以改善准确性。 `re.error` 仍被保留用于向下兼容。
   

### shutil[¶](#shutil "Link to this heading")

*   在 [`chown()`](../library/shutil.html#shutil.chown "shutil.chown") 中增加了对 _dir\_fd_ 和 _follow\_symlinks_ 关键字参数的支持。 （由 Berker Peksag 和 Tahia K 在 [gh-62308](https://github.com/python/cpython/issues/62308) 中贡献。）
   

### site[¶](#site "Link to this heading")

*   现在 `.pth` 文件将先使用 UTF-8 来解码，如果 UTF-8 解码失败再使用 [locale encoding](../glossary.html#term-locale-encoding)。 （由 Inada Naoki 在 [gh-117802](https://github.com/python/cpython/issues/117802) 中贡献。）
   

### sqlite3[¶](#sqlite3 "Link to this heading")

*   现在当一个 [`Connection`](../library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") 对象未被显式地 [`关闭`](../library/sqlite3.html#sqlite3.Connection.close "sqlite3.Connection.close") 时将发出 [`ResourceWarning`](../library/exceptions.html#ResourceWarning "ResourceWarning")。 （由 Erlend E. Aasland 在 [gh-105539](https://github.com/python/cpython/issues/105539) 中贡献。）
   
*   为 [`Connection.iterdump()`](../library/sqlite3.html#sqlite3.Connection.iterdump "sqlite3.Connection.iterdump") 增加了 _filter_ 仅限关键字形参用于过滤要转储的数据库对象。 （由 Mariusz Felisiak 在 [gh-91602](https://github.com/python/cpython/issues/91602) 中贡献。）
   

### ssl[¶](#ssl "Link to this heading")

*   现在 [`create_default_context()`](../library/ssl.html#ssl.create_default_context "ssl.create_default_context") API 将在其默认旗标中包括 [`VERIFY_X509_PARTIAL_CHAIN`](../library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN "ssl.VERIFY_X509_PARTIAL_CHAIN") 和 [`VERIFY_X509_STRICT`](../library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT")。
   
   备注
   
   [`VERIFY_X509_STRICT`](../library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT") 可能会拒绝下层 OpenSSL 实现本来会接受的 [**RFC 5280**](https://datatracker.ietf.org/doc/html/rfc5280.html) 以前的证书或格式错误的证书。 虽然不建议禁用此功能，但你可以使用以下方式禁用它：
   
   import ssl
   
   ctx \= ssl.create\_default\_context()
   ctx.verify\_flags &= ~ssl.VERIFY\_X509\_STRICT
   
   （由 William Woodruff 在 [gh-112389](https://github.com/python/cpython/issues/112389) 贡献。）
   

### statistics[¶](#statistics "Link to this heading")

*   增加了用于核密度估计的 [`kde()`](../library/statistics.html#statistics.kde "statistics.kde")。 这使得根据固定数量的离散样本估计连续概率密度函数成为可能。 （由 Raymond Hettinger 在 [gh-115863](https://github.com/python/cpython/issues/115863) 中贡献。）
   
*   增加了 [`kde_random()`](../library/statistics.html#statistics.kde_random "statistics.kde_random") 用来从 [`kde()`](../library/statistics.html#statistics.kde "statistics.kde") 创建的估计概率密度函数进行取样。 （由 Hettinger 在 [gh-115863](https://github.com/python/cpython/issues/115863) 中贡献。）
   

### subprocess[¶](#subprocess "Link to this heading")

*   现在 [`subprocess`](../library/subprocess.html#module-subprocess "subprocess: Subprocess management.") 模块会在更多场合下使用 [`posix_spawn()`](../library/os.html#os.posix_spawn "os.posix_spawn") 函数。
   
   需要注意的是，当 _close\_fds_ 为 `True` 时（默认值），则将在 C 库提供了 `posix_spawn_file_actions_addclosefrom_np()` 时使用 [`posix_spawn()`](../library/os.html#os.posix_spawn "os.posix_spawn")，这包括近期的 Linux, FreeBSD 和 Solaris 版本。 在 Linux，其性能应当与现有的 Linux `vfork()` 基础代码类似。
   
   如果你需要强制 [`subprocess`](../library/subprocess.html#module-subprocess "subprocess: Subprocess management.") 绝不使用 [`posix_spawn()`](../library/os.html#os.posix_spawn "os.posix_spawn") 可以将私有的控制节点 `subprocess._USE_POSIX_SPAWN` 设为 `False`。 如果你这样设置的话请在 [issue tracker](../bugs.html#using-the-tracker) 中报告你的理由和平台相关的细节以便我们能够为大家改进 API 的选择逻辑。 （由 Jakub Kulik 在 [gh-113117](https://github.com/python/cpython/issues/113117) 中贡献。）
   

### sys[¶](#sys "Link to this heading")

*   增加了 [`_is_interned()`](../library/sys.html#sys._is_interned "sys._is_interned") 函数用于检测字符串是否被内部化。 此函数不保证在所有的 Python 实现中均存在。 （由 Serhiy Storchaka 在 [gh-78573](https://github.com/python/cpython/issues/78573) 中贡献。）
   

### tempfile[¶](#tempfile "Link to this heading")

*   在 Windows 上，[`tempfile.mkdtemp()`](../library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp") 所使用的默认模式 `0o700` 由于 [`os.mkdir()`](../library/os.html#os.mkdir "os.mkdir") 的更改现在将限制对新目录的访问。 这是对 [**CVE 2024-4030**](https://www.cve.org/CVERecord?id=CVE-2024-4030) 的缓解措施。 （由 Steve Dower 在 [gh-118486](https://github.com/python/cpython/issues/118486) 中贡献。）
   

### time[¶](#time "Link to this heading")

*   在 Windows 上，[`monotonic()`](../library/time.html#time.monotonic "time.monotonic") 现在将使用精度为 1 微秒的 `QueryPerformanceCounter()` 时钟，而不是精度只有 15.6 毫秒的 `GetTickCount64()` 时钟。 （由 Victor Stinner 在 [gh-88494](https://github.com/python/cpython/issues/88494) 中贡献。）
   
*   在 Windows 上，[`time()`](../library/time.html#time.time "time.time") 现在将使用精度为 1 微秒的 `GetSystemTimePreciseAsFileTime()` 时钟，代替精度为 15.6 毫秒的 `GetSystemTimeAsFileTime()` 时钟。 （由 Victor Stinner 在 [gh-63207](https://github.com/python/cpython/issues/63207) 中贡献。）
   

### tkinter[¶](#tkinter "Link to this heading")

*   增加了 [`tkinter`](../library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") 控件方法: `tk_busy_hold()`, `tk_busy_configure()`, `tk_busy_cget()`, `tk_busy_forget()`, `tk_busy_current()` 和 `tk_busy_status()`。 （由 Miguel, klappnase 和 Serhiy Storchaka 在 [gh-72684](https://github.com/python/cpython/issues/72684) 中贡献。）
   
*   现在 [`tkinter`](../library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") 控件 `wm_attributes()` 接受不带负号前缀的属性名称来获取窗口属性，例如 `w.wm_attributes('alpha')` 并允许指定属性和值以关键字参数形式来设置，例如 `w.wm_attributes(alpha=0.5)`。 （由 Serhiy Storchaka 在 [gh-43457](https://github.com/python/cpython/issues/43457) 中贡献。）
   
*   通过使用新的可选关键字形参 _return\_python\_dict_，现在 `wm_attributes()` 可将属性作为 [`dict`](../library/stdtypes.html#dict "dict") 返回。 （由 Serhiy Storchaka 在 [gh-43457](https://github.com/python/cpython/issues/43457) 中贡献。）
   
*   现在当使用新的可选仅限关键字形参 _return\_ints_ 时 `Text.count()` 可以返回一个简单的 [`int`](../library/functions.html#int "int")。 在其他情况下，将以 1 个元素的元组形式返回单个计数值或者 `None`。 （由 Serhiy Storchaka 在 [gh-97928](https://github.com/python/cpython/issues/97928) 中贡献。）
   
*   在 [`tkinter.ttk.Style`](../library/tkinter.ttk.html#tkinter.ttk.Style "tkinter.ttk.Style") 的 [`element_create()`](../library/tkinter.ttk.html#tkinter.ttk.Style.element_create "tkinter.ttk.Style.element_create") 方法中增加了对 "vsapi" 元素类型的支持。 （由 Serhiy Storchaka 在 [gh-68166](https://github.com/python/cpython/issues/68166) 中贡献。）
   
*   为 Tkinter 的控件增加了 `after_info()` 方法。 （由 Cheryl Sabella 在 [gh-77020](https://github.com/python/cpython/issues/77020) 中贡献。）
   
*   为 `PhotoImage` 新增 `copy_replace()` 方法用于将一个图像的某个区域拷贝到另一个图像，可能带有像素缩放、子采样，或两者皆有。 （由 Serhiy Storchaka 在 [gh-118225](https://github.com/python/cpython/issues/118225) 中贡献。）
   
*   为 `PhotoImage` 的方法 `copy()`, `zoom()` 和 `subsample()` 增加了 _from\_coords_ 形参。 为 `PhotoImage` 的方法 `copy()` 增加了 _zoom_ 和 _subsample_ 形参。 （由 Serhiy Storchaka 在 [gh-118225](https://github.com/python/cpython/issues/118225) 中贡献。）
   
*   增加了 `PhotoImage` 方法 `read()` 用于从文件读取图像以及 `data()` 用于获取图像数据。 为 `write()` 方法增加了 _background_ 和 _grayscale_ 形参。 （由 Serhiy Storchaka 在 [gh-118271](https://github.com/python/cpython/issues/118271) 中贡献。）.)
   

### 回溯[¶](#traceback "Link to this heading")

*   为 [`TracebackException`](../library/traceback.html#traceback.TracebackException "traceback.TracebackException") 增加了 [`exc_type_str`](../library/traceback.html#traceback.TracebackException.exc_type_str "traceback.TracebackException.exc_type_str") 属性，它用于保存 _exc\_type_ 字符串表示。 弃用了 [`exc_type`](../library/traceback.html#traceback.TracebackException.exc_type "traceback.TracebackException.exc_type") 属性，它用于保存类型对象本身。 增加了 _save\_exc\_type_ 形参 (默认值为 `True`) 用于指明 `exc_type` 是否应当被保存。 （由 Irit Katriel 在 [gh-112332](https://github.com/python/cpython/issues/112332) 中贡献。）
   
*   为 [`TracebackException.format_exception_only()`](../library/traceback.html#traceback.TracebackException.format_exception_only "traceback.TracebackException.format_exception_only") 增加了新的 _show\_group_ 仅限关键字形参用于（递归地）格式化 [`BaseExceptionGroup`](../library/exceptions.html#BaseExceptionGroup "BaseExceptionGroup") 实例中嵌套的异常。 （由 Irit Katriel 在 [gh-105292](https://github.com/python/cpython/issues/105292) 中贡献。）
   

### types[¶](#types "Link to this heading")

*   现在 [`SimpleNamespace`](../library/types.html#types.SimpleNamespace "types.SimpleNamespace") 可以接受单个位置参数来初始化命名空间的各个参数值。 该参数必须为映射或键值对的可迭代对象。 （由 Serhiy Storchaka 在 [gh-108191](https://github.com/python/cpython/issues/108191) 中贡献。）
   

### typing[¶](#typing "Link to this heading")

*   [**PEP 705**](https://peps.python.org/pep-0705/): 增加 [`ReadOnly`](../library/typing.html#typing.ReadOnly "typing.ReadOnly")，一个针对类型检查器的特殊类型结构，用于将 [`TypedDict`](../library/typing.html#typing.TypedDict "typing.TypedDict") 的项标记为只读。
   
*   [**PEP 742**](https://peps.python.org/pep-0742/): 增加 [`TypeIs`](../library/typing.html#typing.TypeIs "typing.TypeIs")，一个可被用于指示类型检查器如何细化类型的类型结构。
   
*   增加 [`NoDefault`](../library/typing.html#typing.NoDefault "typing.NoDefault")，一个用于代表 [`typing`](../library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") 模块中某些形参的默认值的哨兵对象。 （由 Jelle Zijlstra 在 [gh-116126](https://github.com/python/cpython/issues/116126) 中贡献。）
   
*   增加 [`get_protocol_members()`](../library/typing.html#typing.get_protocol_members "typing.get_protocol_members") 用于返回定义一个 [`typing.Protocol`](../library/typing.html#typing.Protocol "typing.Protocol") 的成员的集合。 （由 Jelle Zijlstra 在 [gh-104873](https://github.com/python/cpython/issues/104873) 中贡献。）
   
*   增加 [`is_protocol()`](../library/typing.html#typing.is_protocol "typing.is_protocol") 用于检查一个类是否属于 [`Protocol`](../library/typing.html#typing.Protocol "typing.Protocol")。 （由 Jelle Zijlstra 在 [gh-104873](https://github.com/python/cpython/issues/104873) 中贡献。）
   
*   现在 [`ClassVar`](../library/typing.html#typing.ClassVar "typing.ClassVar") 可以被嵌套在 [`Final`](../library/typing.html#typing.Final "typing.Final") 中，反之亦然。 （由 Mehdi Drissi 在 [gh-89547](https://github.com/python/cpython/issues/89547) 中贡献。）
   

### unicodedata[¶](#unicodedata "Link to this heading")

*   将 Unicode 数据库更新到 [15.1.0 版](https://www.unicode.org/versions/Unicode15.1.0/)。 （由 James Gerity 在 [gh-109559](https://github.com/python/cpython/issues/109559) 中贡献。）
   

### venv[¶](#venv "Link to this heading")

*   增加了对在虚拟环境目录中添加源码控制管理 (SCM) 忽略文件的支持。 在默认情况下，Git 已受到支持。 此特性是以可被扩展为支持其他 SCM 的通过 API 选择启用 ([`EnvBuilder`](../library/venv.html#venv.EnvBuilder "venv.EnvBuilder") 和 [`create()`](../library/venv.html#venv.create "venv.create"))，并通过 CLI 使用 `--without-scm-ignore-files` 选择禁用的方式实现的。 （由 Brett Cannon 在 [gh-108125](https://github.com/python/cpython/issues/108125) 中贡献。）
   

### warnings[¶](#warnings "Link to this heading")

*   [**PEP 702**](https://peps.python.org/pep-0702/): 新的 [`warnings.deprecated()`](../library/warnings.html#warnings.deprecated "warnings.deprecated") 装饰器提供了一种将弃用消息传送给 [static type checker](../glossary.html#term-static-type-checker) 并在使用已弃用的类和函数时发出警告的方式。 当被装饰的函数或类在运行时被使用时也可以发出 [`DeprecationWarning`](../library/exceptions.html#DeprecationWarning "DeprecationWarning")。 （由 Jelle Zijlstra 在 [gh-104003](https://github.com/python/cpython/issues/104003) 中贡献。）
   

### xml[¶](#xml "Link to this heading")

*   通过添加五个新方法来允许控制 Expat >=2.6.0 重解析延迟 ([**CVE 2023-52425**](https://www.cve.org/CVERecord?id=CVE-2023-52425))：
   
   *   [`xml.etree.ElementTree.XMLParser.flush()`](../library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.flush "xml.etree.ElementTree.XMLParser.flush")
       
   *   [`xml.etree.ElementTree.XMLPullParser.flush()`](../library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.flush "xml.etree.ElementTree.XMLPullParser.flush")
       
   *   [`xml.parsers.expat.xmlparser.GetReparseDeferralEnabled()`](../library/pyexpat.html#xml.parsers.expat.xmlparser.GetReparseDeferralEnabled "xml.parsers.expat.xmlparser.GetReparseDeferralEnabled")
       
   *   [`xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()`](../library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled "xml.parsers.expat.xmlparser.SetReparseDeferralEnabled")
       
   *   `xml.sax.expatreader.ExpatParser.flush()`
       
   
   （由 Sebastian Pipping 在 [gh-115623](https://github.com/python/cpython/issues/115623) 中贡献。）
   
*   为 [`iterparse()`](../library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse "xml.etree.ElementTree.iterparse") 所返回的迭代器增加了 `close()` 方法用于执行显式的清理。 （由 Serhiy Storchaka 在 [gh-69893](https://github.com/python/cpython/issues/69893) 中贡献。）
   

### zipimport[¶](#zipimport "Link to this heading")

*   增加了对 [ZIP64](https://en.wikipedia.org/wiki/Zip_(file_format)#ZIP64) 格式的文件的支持。 大家都喜欢更庞大的数据，对吧？ （由 Tim Hatch 在 [gh-94146](https://github.com/python/cpython/issues/94146) 中贡献。）.)
   

性能优化[¶](#optimizations "Link to this heading")
----------------------------------------------

*   一些标准库模块的导入时间得到了显著改善。 例如，[`typing`](../library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") 模块的导入时间通过移除对 [`re`](../library/re.html#module-re "re: Regular expression operations.") 和 [`contextlib`](../library/contextlib.html#module-contextlib "contextlib: Utilities for with-statement contexts.") 的依赖而减少了大约三分之一。 其他获得导入时间加速的模块包括 [`email.utils`](../library/email.utils.html#module-email.utils "email.utils: Miscellaneous email package utilities."), [`enum`](../library/enum.html#module-enum "enum: Implementation of an enumeration class."), [`functools`](../library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects."), [`importlib.metadata`](../library/importlib.metadata.html#module-importlib.metadata "importlib.metadata: Accessing package metadata") 和 [`threading`](../library/threading.html#module-threading "threading: Thread-based parallelism.")。 （由 Alex Waygood, Shantanu Jain, Adam Turner, Daniel Hollas 等人在 [gh-109653](https://github.com/python/cpython/issues/109653) 中贡献。）
   
*   现在对于大量输入 [`textwrap.indent()`](../library/textwrap.html#textwrap.indent "textwrap.indent") 相比之前可提速大约 30%。 （由 Inada Naoki 在 [gh-107369](https://github.com/python/cpython/issues/107369) 中贡献。）
   
*   现在 [`subprocess`](../library/subprocess.html#module-subprocess "subprocess: Subprocess management.") 模块会在更多场合下使用 [`posix_spawn()`](../library/os.html#os.posix_spawn "os.posix_spawn") 函数，包括在许多现代系统平台上当 _close\_fds_ 为 `True` (默认值) 的时候。 当在 FreeBSD 和 Solaris 上启动进程时这应该能提供显著的性能提升。 请参阅上面的 [subprocess](#whatsnew313-subprocess) 小节了解详情。 （由 Jakub Kulik 在 [gh-113117](https://github.com/python/cpython/issues/113117) 中贡献。）
   

被移除的模块与 API[¶](#removed-modules-and-apis "Link to this heading")
----------------------------------------------------------------

### PEP 594: 从标准库中移除“死电池”[¶](#pep-594-remove-dead-batteries-from-the-standard-library "Link to this heading")

[**PEP 594**](https://peps.python.org/pep-0594/) 提议从标准库移除 19 个模块，它们因其古旧、过时或不安全的状态而被非正式地称呼为‘死电池’。 下列所有模块在 Python 3.11 中被弃用，现在已被移除：

*   `aifc`
   
*   `audioop`
   
*   `chunk`
   
*   `cgi` 和 `cgitb`
   
   *   对于 `GET` 和 `HEAD` 请求 `cgi.FieldStorage` 通常可以用 [`urllib.parse.parse_qsl()`](../library/urllib.parse.html#urllib.parse.parse_qsl "urllib.parse.parse_qsl") 来替换，而对于 `POST` 和 `PUT` 请求则可以用 [`email.message`](../library/email.message.html#module-email.message "email.message: The base class representing email messages.") 模块或 [multipart](https://pypi.org/project/multipart/) 库。
       
   *   `cgi.parse()` 可被替换为在想要的查询字符串上直接调用 [`urllib.parse.parse_qs()`](../library/urllib.parse.html#urllib.parse.parse_qs "urllib.parse.parse_qs")，除非输入为 `multipart/form-data`，它应当如下文针对 `cgi.parse_multipart()` 所描述的那样被替换。
       
   *   `cgi.parse_header()` 可被 [`email`](../library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.") 包中的功能所替换，它实现了相同的 MIME RFC。 例如，使用 [`email.message.EmailMessage`](../library/email.message.html#email.message.EmailMessage "email.message.EmailMessage"):
       
       from email.message import EmailMessage
       
       msg \= EmailMessage()
       msg\['content-type'\] \= 'application/json; charset="utf8"'
       main, params \= msg.get\_content\_type(), msg\['content-type'\].params
       
   *   `cgi.parse_multipart()` can be replaced with the functionality in the [`email`](../library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.") package, which implements the same MIME RFCs, or with the [multipart](https://pypi.org/project/multipart/) library. For example, the [`email.message.EmailMessage`](../library/email.message.html#email.message.EmailMessage "email.message.EmailMessage") and [`email.message.Message`](../library/email.compat32-message.html#email.message.Message "email.message.Message") classes.
       
*   `crypt` and the private `_crypt` extension. The [`hashlib`](../library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.") module may be an appropriate replacement when simply hashing a value is required. Otherwise, various third-party libraries on PyPI are available:
   
   *   [bcrypt](https://pypi.org/project/bcrypt/): 用于软件和服务器的现代密码哈希算法。
       
   *   [passlib](https://pypi.org/project/passlib/): 支持超过 over 30 种方案的综合密码哈希算法框架。
       
   *   [argon2-cffi](https://pypi.org/project/argon2-cffi/): 安全的 Argon2 密码哈希算法。
       
   *   [legacycrypt](https://pypi.org/project/legacycrypt/): 针对 POSIX 加密库调用和相关功能的 [`ctypes`](../library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.") 包装器。
       
   *   [crypt\_r](https://pypi.org/project/crypt_r/): `crypt` 模块的分叉，针对 _[crypt\_r(3)](https://manpages.debian.org/crypt_r(3))_ 库调用和相关功能和包装器。
       
*   `imghdr`: The [filetype](https://pypi.org/project/filetype/), [puremagic](https://pypi.org/project/puremagic/), or [python-magic](https://pypi.org/project/python-magic/) libraries should be used as replacements. For example, the `puremagic.what()` function can be used to replace the `imghdr.what()` function for all file formats that were supported by `imghdr`.
   
*   `mailcap`: 改用 [`mimetypes`](../library/mimetypes.html#module-mimetypes "mimetypes: Mapping of filename extensions to MIME types.") 模块。
   
*   `msilib`
   
*   `nis`
   
*   `nntplib`: 改用 PyPI 上的 [pynntp](https://pypi.org/project/pynntp/) 库。
   
*   `ossaudiodev`: 对于音频回放，改用 PyPI 上的 [pygame](https://pypi.org/project/pygame/) 库。
   
*   `pipes`: 改用 [`subprocess`](../library/subprocess.html#module-subprocess "subprocess: Subprocess management.") 模块。
   
*   `sndhdr`: 应当使用 [filetype](https://pypi.org/project/filetype/), [puremagic](https://pypi.org/project/puremagic/) 或 [python-magic](https://pypi.org/project/python-magic/) 库作为替代。
   
*   `spwd`: 改用 PyPI 上的 [python-pam](https://pypi.org/project/python-pam/) 库。
   
*   `sunau`
   
*   `telnetlib`，改用 PyPI 上的 [telnetlib3](https://pypi.org/project/telnetlib3/) 或 [Exscript](https://pypi.org/project/Exscript/) 库。
   
*   `uu`: 改用 the [`base64`](../library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85") 模块，作为一款现代化的替代。
   
*   `xdrlib`
   

（由 Victor Stinner 和 Zachary Ware 在 [gh-104773](https://github.com/python/cpython/issues/104773) 和 [gh-104780](https://github.com/python/cpython/issues/104780) 中贡献。）

### 2to3[¶](#to3 "Link to this heading")

*   移除 **2to3** 程序和 `lib2to3` 模块，此前已在 Python 3.11 中被弃用。 （由 Victor Stinner 在 [gh-104780](https://github.com/python/cpython/issues/104780) 中贡献。）
   

### builtins[¶](#builtins "Link to this heading")

*   Remove support for chained [`classmethod`](../library/functions.html#classmethod "classmethod") descriptors (introduced in [gh-63272](https://github.com/python/cpython/issues/63272)). These can no longer be used to wrap other descriptors, such as [`property`](../library/functions.html#property "property"). The core design of this feature was flawed and led to several problems. To "pass-through" a [`classmethod`](../library/functions.html#classmethod "classmethod"), consider using the `__wrapped__` attribute that was added in Python 3.10. (Contributed by Raymond Hettinger in [gh-89519](https://github.com/python/cpython/issues/89519).)
   
*   Raise a [`RuntimeError`](../library/exceptions.html#RuntimeError "RuntimeError") when calling [`frame.clear()`](../reference/datamodel.html#frame.clear "frame.clear") on a suspended frame (as has always been the case for an executing frame). (Contributed by Irit Katriel in [gh-79932](https://github.com/python/cpython/issues/79932).)
   

### configparser[¶](#id3 "Link to this heading")

*   Remove the undocumented `LegacyInterpolation` class, deprecated in the docstring since Python 3.2, and at runtime since Python 3.11. (Contributed by Hugo van Kemenade in [gh-104886](https://github.com/python/cpython/issues/104886).)
   

### importlib.metadata[¶](#importlib-metadata "Link to this heading")

*   Remove deprecated subscript ([`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__")) access for [EntryPoint](../library/importlib.metadata.html#entry-points) objects. (Contributed by Jason R. Coombs in [gh-113175](https://github.com/python/cpython/issues/113175).)
   

### locale[¶](#locale "Link to this heading")

*   Remove the `locale.resetlocale()` function, deprecated in Python 3.11. Use `locale.setlocale(locale.LC_ALL, "")` instead. (Contributed by Victor Stinner in [gh-104783](https://github.com/python/cpython/issues/104783).)
   

### opcode[¶](#opcode "Link to this heading")

*   Move `opcode.ENABLE_SPECIALIZATION` to `_opcode.ENABLE_SPECIALIZATION`. This field was added in 3.12, it was never documented, and is not intended for external use. (Contributed by Irit Katriel in [gh-105481](https://github.com/python/cpython/issues/105481).)
   
*   Remove `opcode.is_pseudo()`, `opcode.MIN_PSEUDO_OPCODE`, and `opcode.MAX_PSEUDO_OPCODE`, which were added in Python 3.12, but were neither documented nor exposed through [`dis`](../library/dis.html#module-dis "dis: Disassembler for Python bytecode."), and were not intended to be used externally. (Contributed by Irit Katriel in [gh-105481](https://github.com/python/cpython/issues/105481).)
   

### pathlib[¶](#id4 "Link to this heading")

*   移除了使用 [`Path`](../library/pathlib.html#pathlib.Path "pathlib.Path") 对象作为上下文管理器的能力。 此功能自 Python 3.9 起已被弃用并设为空操作。 （由 Barney Gale 在 [gh-83863](https://github.com/python/cpython/issues/83863) 中贡献。）
   

### re[¶](#id5 "Link to this heading")

*   移除了未被写入文档、已被弃用且已不能工作的 `re.template()` 函数和 `re.TEMPLATE` / `re.T` 旗标。 （由 Serhiy Storchaka 和 Nikita Sobolev 在 [gh-105687](https://github.com/python/cpython/issues/105687) 中贡献。）
   

### tkinter.tix[¶](#tkinter-tix "Link to this heading")

*   移除了 `tkinter.tix` 模块，它在 Python 3.6 中已被弃用。 该模块所包装的第三方库 Tix 已不再维护。 （由 Zachary Ware 在 [gh-75552](https://github.com/python/cpython/issues/75552) 中贡献。）.)
   

### turtle[¶](#turtle "Link to this heading")

*   Remove the `RawTurtle.settiltangle()` method, deprecated in the documentation since Python 3.1 and at runtime since Python 3.11. (Contributed by Hugo van Kemenade in [gh-104876](https://github.com/python/cpython/issues/104876).)
   

### typing[¶](#id6 "Link to this heading")

*   Remove the `typing.io` and `typing.re` namespaces, deprecated since Python 3.8. The items in those namespaces can be imported directly from the [`typing`](../library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") module. (Contributed by Sebastian Rittau in [gh-92871](https://github.com/python/cpython/issues/92871).)
   
*   移除了创建 [`TypedDict`](../library/typing.html#typing.TypedDict "typing.TypedDict") 类型的关键字参数方法，它在 Python 3.11 中已被弃用。 （由 Tomas Roun 在 [gh-104786](https://github.com/python/cpython/issues/104786) 中贡献。）
   

### unittest[¶](#unittest "Link to this heading")

*   移除了下列 [`unittest`](../library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") 函数，它们在 Python 3.11 中已被弃用：
   
   *   `unittest.findTestCases()`
       
   *   `unittest.makeSuite()`
       
   *   `unittest.getTestCaseNames()`
       
   
   请改用 [`TestLoader`](../library/unittest.html#unittest.TestLoader "unittest.TestLoader") 方法:
   
   *   [`loadTestsFromModule()`](../library/unittest.html#unittest.TestLoader.loadTestsFromModule "unittest.TestLoader.loadTestsFromModule")
       
   *   [`loadTestsFromTestCase()`](../library/unittest.html#unittest.TestLoader.loadTestsFromTestCase "unittest.TestLoader.loadTestsFromTestCase")
       
   *   [`getTestCaseNames()`](../library/unittest.html#unittest.TestLoader.getTestCaseNames "unittest.TestLoader.getTestCaseNames")
       
   
   （由 Hugo van Kemenade 在 [gh-104835](https://github.com/python/cpython/issues/104835) 中贡献。）
   
*   Remove the untested and undocumented `TestProgram.usageExit()` method, deprecated in Python 3.11. (Contributed by Hugo van Kemenade in [gh-104992](https://github.com/python/cpython/issues/104992).)
   

### urllib[¶](#urllib "Link to this heading")

*   Remove the _cafile_, _capath_, and _cadefault_ parameters of the [`urllib.request.urlopen()`](../library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") function, deprecated in Python 3.6. Use the _context_ parameter instead with an [`SSLContext`](../library/ssl.html#ssl.SSLContext "ssl.SSLContext") instance. The [`ssl.SSLContext.load_cert_chain()`](../library/ssl.html#ssl.SSLContext.load_cert_chain "ssl.SSLContext.load_cert_chain") function can be used to load specific certificates, or let [`ssl.create_default_context()`](../library/ssl.html#ssl.create_default_context "ssl.create_default_context") select the operating system's trusted certificate authority (CA) certificates. (Contributed by Victor Stinner in [gh-105382](https://github.com/python/cpython/issues/105382).)
   

### webbrowser[¶](#webbrowser "Link to this heading")

*   Remove the untested and undocumented `MacOSX` class, deprecated in Python 3.11. Use the `MacOSXOSAScript` class (introduced in Python 3.2) instead. (Contributed by Hugo van Kemenade in [gh-104804](https://github.com/python/cpython/issues/104804).)
   
*   Remove the deprecated `MacOSXOSAScript._name` attribute. Use the [`MacOSXOSAScript.name`](../library/webbrowser.html#webbrowser.controller.name "webbrowser.controller.name") attribute instead. (Contributed by Nikita Sobolev in [gh-105546](https://github.com/python/cpython/issues/105546).)
   

新的弃用[¶](#new-deprecations "Link to this heading")
-------------------------------------------------

*   [用户自定义函数](../reference/datamodel.html#user-defined-funcs):
   
   *   Deprecate assignment to a function's [`__code__`](../reference/datamodel.html#function.__code__ "function.__code__") attribute, where the new code object's type does not match the function's type. The different types are: plain function, generator, async generator, and coroutine. (Contributed by Irit Katriel in [gh-81137](https://github.com/python/cpython/issues/81137).)
       
*   [`array`](../library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values."):
   
   *   Deprecate the `'u'` format code (`wchar_t`) at runtime. This format code has been deprecated in documentation since Python 3.3, and will be removed in Python 3.16. Use the `'w'` format code ([`Py_UCS4`](../c-api/unicode.html#c.Py_UCS4 "Py_UCS4")) for Unicode characters instead. (Contributed by Hugo van Kemenade in [gh-80480](https://github.com/python/cpython/issues/80480).)
       
*   [`ctypes`](../library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python."):
   
   *   Deprecate the undocumented `SetPointerType()` function, to be removed in Python 3.15. (Contributed by Victor Stinner in [gh-105733](https://github.com/python/cpython/issues/105733).)
       
   *   [Soft-deprecate](../glossary.html#term-soft-deprecated) the [`ARRAY()`](../library/ctypes.html#ctypes.ARRAY "ctypes.ARRAY") function in favour of `type * length` multiplication. (Contributed by Victor Stinner in [gh-105733](https://github.com/python/cpython/issues/105733).)
       
*   [`decimal`](../library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic  Specification."):
   
   *   Deprecate the non-standard and undocumented [`Decimal`](../library/decimal.html#decimal.Decimal "decimal.Decimal") format specifier `'N'`, which is only supported in the `decimal` module's C implementation. (Contributed by Serhiy Storchaka in [gh-89902](https://github.com/python/cpython/issues/89902).)
       
*   [`dis`](../library/dis.html#module-dis "dis: Disassembler for Python bytecode."):
   
   *   Deprecate the `HAVE_ARGUMENT` separator. Check membership in [`hasarg`](../library/dis.html#dis.hasarg "dis.hasarg") instead. (Contributed by Irit Katriel in [gh-109319](https://github.com/python/cpython/issues/109319).)
       
*   [`getopt`](../library/getopt.html#module-getopt "getopt: Portable parser for command line options; support both short and long option names.") and [`optparse`](../library/optparse.html#module-optparse "optparse: Command-line option parsing library.（已弃用）"):
   
   *   Both modules are now [soft deprecated](../glossary.html#term-soft-deprecated), with [`argparse`](../library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.") preferred for new projects. This is a new soft-deprecation for the `getopt` module, whereas the `optparse` module was already _de facto_ soft deprecated. (Contributed by Victor Stinner in [gh-106535](https://github.com/python/cpython/issues/106535).)
       
*   [`gettext`](../library/gettext.html#module-gettext "gettext: Multilingual internationalization services."):
   
   *   Deprecate non-integer numbers as arguments to functions and methods that consider plural forms in the `gettext` module, even if no translation was found. (Contributed by Serhiy Storchaka in [gh-88434](https://github.com/python/cpython/issues/88434).)
       
*   [`glob`](../library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion."):
   
   *   Deprecate the undocumented `glob0()` and `glob1()` functions. Use [`glob()`](../library/glob.html#glob.glob "glob.glob") and pass a [path-like object](../glossary.html#term-path-like-object) specifying the root directory to the _root\_dir_ parameter instead. (Contributed by Barney Gale in [gh-117337](https://github.com/python/cpython/issues/117337).)
       
*   [`http.server`](../library/http.server.html#module-http.server "http.server: HTTP server and request handlers."):
   
   *   Deprecate [`CGIHTTPRequestHandler`](../library/http.server.html#http.server.CGIHTTPRequestHandler "http.server.CGIHTTPRequestHandler"), to be removed in Python 3.15. Process-based CGI HTTP servers have been out of favor for a very long time. This code was outdated, unmaintained, and rarely used. It has a high potential for both security and functionality bugs. (Contributed by Gregory P. Smith in [gh-109096](https://github.com/python/cpython/issues/109096).)
       
   *   Deprecate the `--cgi` flag to the **python -m http.server** command-line interface, to be removed in Python 3.15. (Contributed by Gregory P. Smith in [gh-109096](https://github.com/python/cpython/issues/109096).)
       
*   [`mimetypes`](../library/mimetypes.html#module-mimetypes "mimetypes: Mapping of filename extensions to MIME types."):
   
   *   [Soft-deprecate](../glossary.html#term-soft-deprecated) file path arguments to [`guess_type()`](../library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type"), use [`guess_file_type()`](../library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type") instead. (Contributed by Serhiy Storchaka in [gh-66543](https://github.com/python/cpython/issues/66543).)
       
*   [`re`](../library/re.html#module-re "re: Regular expression operations."):
   
   *   Deprecate passing the optional _maxsplit_, _count_, or _flags_ arguments as positional arguments to the module-level [`split()`](../library/re.html#re.split "re.split"), [`sub()`](../library/re.html#re.sub "re.sub"), and [`subn()`](../library/re.html#re.subn "re.subn") functions. These parameters will become [keyword-only](../glossary.html#keyword-only-parameter) in a future version of Python. (Contributed by Serhiy Storchaka in [gh-56166](https://github.com/python/cpython/issues/56166).)
       
*   [`pathlib`](../library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths"):
   
   *   Deprecate [`PurePath.is_reserved()`](../library/pathlib.html#pathlib.PurePath.is_reserved "pathlib.PurePath.is_reserved"), to be removed in Python 3.15. Use [`os.path.isreserved()`](../library/os.path.html#os.path.isreserved "os.path.isreserved") to detect reserved paths on Windows. (Contributed by Barney Gale in [gh-88569](https://github.com/python/cpython/issues/88569).)
       
*   [`platform`](../library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible."):
   
   *   弃用了 [`java_ver()`](../library/platform.html#platform.java_ver "platform.java_ver")，并将在 Python 3.15 中移除。 此函数仅对 Jython 支持有用，具有令人困惑的 API，并且大部分未经测试。 （由 Nikita Sobolev 在 [gh-116349](https://github.com/python/cpython/issues/116349) 中贡献。）.)
       
*   [`pydoc`](../library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system."):
   
   *   弃用未写入文档的 `ispackage()` 函数。 （由 Zackery Spytz 在 [gh-64020](https://github.com/python/cpython/issues/64020) 中贡献。）
       
*   [`sqlite3`](../library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x."):
   
   *   Deprecate passing more than one positional argument to the [`connect()`](../library/sqlite3.html#sqlite3.connect "sqlite3.connect") function and the [`Connection`](../library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") constructor. The remaining parameters will become keyword-only in Python 3.15. (Contributed by Erlend E. Aasland in [gh-107948](https://github.com/python/cpython/issues/107948).)
       
   *   Deprecate passing name, number of arguments, and the callable as keyword arguments for [`Connection.create_function()`](../library/sqlite3.html#sqlite3.Connection.create_function "sqlite3.Connection.create_function") and [`Connection.create_aggregate()`](../library/sqlite3.html#sqlite3.Connection.create_aggregate "sqlite3.Connection.create_aggregate") These parameters will become positional-only in Python 3.15. (Contributed by Erlend E. Aasland in [gh-108278](https://github.com/python/cpython/issues/108278).)
       
   *   Deprecate passing the callback callable by keyword for the [`set_authorizer()`](../library/sqlite3.html#sqlite3.Connection.set_authorizer "sqlite3.Connection.set_authorizer"), [`set_progress_handler()`](../library/sqlite3.html#sqlite3.Connection.set_progress_handler "sqlite3.Connection.set_progress_handler"), and [`set_trace_callback()`](../library/sqlite3.html#sqlite3.Connection.set_trace_callback "sqlite3.Connection.set_trace_callback") [`Connection`](../library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") methods. The callback callables will become positional-only in Python 3.15. (Contributed by Erlend E. Aasland in [gh-108278](https://github.com/python/cpython/issues/108278).)
       
*   [`sys`](../library/sys.html#module-sys "sys: Access system-specific parameters and functions."):
   
   *   Deprecate the [`_enablelegacywindowsfsencoding()`](../library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding") function, to be removed in Python 3.16. Use the [`PYTHONLEGACYWINDOWSFSENCODING`](../using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable instead. (Contributed by Inada Naoki in [gh-73427](https://github.com/python/cpython/issues/73427).)
       
*   [`tarfile`](../library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files."):
   
   *   弃用了未写入文档也未被使用的 `TarFile.tarfile` 属性，并将在 Python 3.16 中移除。 （在 [gh-115256](https://github.com/python/cpython/issues/115256) 中贡献。）
       
*   [`traceback`](../library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback."):
   
   *   已弃用 [`TracebackException.exc_type`](../library/traceback.html#traceback.TracebackException.exc_type "traceback.TracebackException.exc_type") 属性。 请改用 [`TracebackException.exc_type_str`](../library/traceback.html#traceback.TracebackException.exc_type_str "traceback.TracebackException.exc_type_str")。 （由 Irit Katriel 在 [gh-112332](https://github.com/python/cpython/issues/112332) 中贡献。）
       
*   [`typing`](../library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`)."):
   
   *   Deprecate the undocumented keyword argument syntax for creating [`NamedTuple`](../library/typing.html#typing.NamedTuple "typing.NamedTuple") classes (e.g. `Point = NamedTuple("Point", x=int, y=int)`), to be removed in Python 3.15. Use the class-based syntax or the functional syntax instead. (Contributed by Alex Waygood in [gh-105566](https://github.com/python/cpython/issues/105566).)
       
   *   Deprecate omitting the _fields_ parameter when creating a [`NamedTuple`](../library/typing.html#typing.NamedTuple "typing.NamedTuple") or [`typing.TypedDict`](../library/typing.html#typing.TypedDict "typing.TypedDict") class, and deprecate passing `None` to the _fields_ parameter of both types. Python 3.15 will require a valid sequence for the _fields_ parameter. To create a NamedTuple class with zero fields, use `class NT(NamedTuple): pass` or `NT = NamedTuple("NT", ())`. To create a TypedDict class with zero fields, use `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`. (Contributed by Alex Waygood in [gh-105566](https://github.com/python/cpython/issues/105566) and [gh-105570](https://github.com/python/cpython/issues/105570).)
       
   *   Deprecate the [`typing.no_type_check_decorator()`](../library/typing.html#typing.no_type_check_decorator "typing.no_type_check_decorator") decorator function, to be removed in in Python 3.15. After eight years in the [`typing`](../library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") module, it has yet to be supported by any major type checker. (Contributed by Alex Waygood in [gh-106309](https://github.com/python/cpython/issues/106309).)
       
   *   Deprecate [`typing.AnyStr`](../library/typing.html#typing.AnyStr "typing.AnyStr"). In Python 3.16, it will be removed from `typing.__all__`, and a [`DeprecationWarning`](../library/exceptions.html#DeprecationWarning "DeprecationWarning") will be emitted at runtime when it is imported or accessed. It will be removed entirely in Python 3.18. Use the new [type parameter syntax](../reference/compound_stmts.html#type-params) instead. (Contributed by Michael The in [gh-107116](https://github.com/python/cpython/issues/107116).)
       
*   [`wave`](../library/wave.html#module-wave "wave: Provide an interface to the WAV sound format."):
   
   *   Deprecate the [`getmark()`](../library/wave.html#wave.Wave_read.getmark "wave.Wave_read.getmark"), `setmark()`, and [`getmarkers()`](../library/wave.html#wave.Wave_read.getmarkers "wave.Wave_read.getmarkers") methods of the [`Wave_read`](../library/wave.html#wave.Wave_read "wave.Wave_read") and [`Wave_write`](../library/wave.html#wave.Wave_write "wave.Wave_write") classes, to be removed in Python 3.15. (Contributed by Victor Stinner in [gh-105096](https://github.com/python/cpython/issues/105096).)
       

### Pending removal in Python 3.14[¶](#pending-removal-in-python-3-14 "Link to this heading")

*   [`argparse`](../library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library."): `argparse.BooleanOptionalAction` 的 _type_, _choices_ 和 _metavar_ 形参已被弃用并将在 3.14 中移除。 （由 Nikita Sobolev 在 [gh-92248](https://github.com/python/cpython/issues/92248) 中贡献。）
   
*   [`ast`](../library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation."): 以下特性自 Python 3.8 起已在文档中声明弃用，现在当运行时如果它们被访问或使用时将发出 [`DeprecationWarning`](../library/exceptions.html#DeprecationWarning "DeprecationWarning")，并将在 Python 3.14 中移除：
   
   *   `ast.Num`
       
   *   `ast.Str`
       
   *   `ast.Bytes`
       
   *   `ast.NameConstant`
       
   *   `ast.Ellipsis`
       
   
   请改用 [`ast.Constant`](../library/ast.html#ast.Constant "ast.Constant")。 （由 Serhiy Storchaka 在 [gh-90953](https://github.com/python/cpython/issues/90953) 中贡献。）
   
*   [`asyncio`](../library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O."):
   
   *   The child watcher classes `asyncio.MultiLoopChildWatcher`, `asyncio.FastChildWatcher`, `asyncio.AbstractChildWatcher` and `asyncio.SafeChildWatcher` are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)
       
   *   `asyncio.set_child_watcher()`, `asyncio.get_child_watcher()`, `asyncio.AbstractEventLoopPolicy.set_child_watcher()` and `asyncio.AbstractEventLoopPolicy.get_child_watcher()` are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)
       
   *   现在默认事件循环策略的 [`get_event_loop()`](../library/asyncio-eventloop.html#asyncio.get_event_loop "asyncio.get_event_loop") 方法在当前事件循环未设置并决定创建一个时将发出 [`DeprecationWarning`](../library/exceptions.html#DeprecationWarning "DeprecationWarning")。 （由 Serhiy Storchaka 和 Guido van Rossum 在 [gh-100160](https://github.com/python/cpython/issues/100160) 中贡献。）
       
*   [`collections.abc`](../library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers"): Deprecated `collections.abc.ByteString`. Prefer `Sequence` or [`Buffer`](../library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer"). For use in typing, prefer a union, like `bytes | bytearray`, or [`collections.abc.Buffer`](../library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer"). (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)
   
*   [`email`](../library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages."): 已弃用 [`email.utils.localtime()`](../library/email.utils.html#email.utils.localtime "email.utils.localtime") 中的 _isdst_ 形参。 （由 Alan Williams 在 [gh-72346](https://github.com/python/cpython/issues/72346) 中贡献。）
   
*   [`importlib.abc`](../library/importlib.html#module-importlib.abc "importlib.abc: Abstract base classes related to import") 中已弃用的类：
   
   *   `importlib.abc.ResourceReader`
       
   *   `importlib.abc.Traversable`
       
   *   `importlib.abc.TraversableResources`
       
   
   使用 [`importlib.resources.abc`](../library/importlib.resources.abc.html#module-importlib.resources.abc "importlib.resources.abc: Abstract base classes for resources") 类代替:
   
   *   [`importlib.resources.abc.Traversable`](../library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable")
       
   *   [`importlib.resources.abc.TraversableResources`](../library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources "importlib.resources.abc.TraversableResources")
       
   
   （由 Jason R. Coombs 和 Hugo van Kemenade 在 [gh-93963](https://github.com/python/cpython/issues/93963) 中贡献。）
   
*   [`itertools`](../library/itertools.html#module-itertools "itertools: Functions creating iterators for efficient looping.") 具有对 copy, deepcopy 和 pickle 等操作的未写入文档的、低效的、历史上充满问题的且不稳定的支持。 这将在 3.14 中移除以显著减少代码量和维护负担。 （由 Raymond Hettinger 在 [gh-101588](https://github.com/python/cpython/issues/101588) 中贡献。）
   
*   [`multiprocessing`](../library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism."): 默认的启动方法在目前默认使用 `'fork'` 的 Linux, BSD 和其他非 macOS POSIX 平台上将改为更安全的方法 ([gh-84559](https://github.com/python/cpython/issues/84559))。 为此添加运行时警告将带来糟糕的体验因为大部分代码并不会关心这个问题。 当你的代码 _需要_ `'fork'` 时请使用 [`get_context()`](../library/multiprocessing.html#multiprocessing.get_context "multiprocessing.get_context") 或 [`set_start_method()`](../library/multiprocessing.html#multiprocessing.set_start_method "multiprocessing.set_start_method") API 来显式地指明。 参见 [上下文和启动方法](../library/multiprocessing.html#multiprocessing-start-methods)。
   
*   [`pathlib`](../library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths"): [`is_relative_to()`](../library/pathlib.html#pathlib.PurePath.is_relative_to "pathlib.PurePath.is_relative_to") 和 [`relative_to()`](../library/pathlib.html#pathlib.PurePath.relative_to "pathlib.PurePath.relative_to"): 传入额外参数的做法已被弃用。
   
*   [`pkgutil`](../library/pkgutil.html#module-pkgutil "pkgutil: Utilities for the import system."): `pkgutil.find_loader()` and :func:!pkgutil.get\_loader\` now raise [`DeprecationWarning`](../library/exceptions.html#DeprecationWarning "DeprecationWarning"); use [`importlib.util.find_spec()`](../library/importlib.html#importlib.util.find_spec "importlib.util.find_spec") instead. (Contributed by Nikita Sobolev in [gh-97850](https://github.com/python/cpython/issues/97850).)
   
*   [`pty`](../library/pty.html#module-pty "pty: Pseudo-Terminal Handling for Unix. (Unix)"):
   
   *   `master_open()`: 使用 [`pty.openpty()`](../library/pty.html#pty.openpty "pty.openpty")。
       
   *   `slave_open()`: 使用 [`pty.openpty()`](../library/pty.html#pty.openpty "pty.openpty")。
       
*   [`sqlite3`](../library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x."):
   
   *   `version` and `version_info`.
       
   *   如果使用了 [命名占位符](../library/sqlite3.html#sqlite3-placeholders) 且 _parameters_ 是一个序列而不是 [`dict`](../library/stdtypes.html#dict "dict") 则选择 [`execute()`](../library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") 和 [`executemany()`](../library/sqlite3.html#sqlite3.Cursor.executemany "sqlite3.Cursor.executemany")。
       
*   [`typing`](../library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`)."): `typing.ByteString`, deprecated since Python 3.9, now causes a [`DeprecationWarning`](../library/exceptions.html#DeprecationWarning "DeprecationWarning") to be emitted when it is used.
   
*   [`urllib`](../library/urllib.html#module-urllib "urllib"): `urllib.parse.Quoter` 已被弃用：它不应被作为公有 API。 （由 Gregory P. Smith 在 [gh-88168](https://github.com/python/cpython/issues/88168) 中贡献。）
   

### Pending removal in Python 3.15[¶](#pending-removal-in-python-3-15 "Link to this heading")

*   导入系统：
   
   *   当设置 [`__spec__.cached`](../library/importlib.html#importlib.machinery.ModuleSpec.cached "importlib.machinery.ModuleSpec.cached") 失败时在模块上设置 [`__cached__`](../reference/datamodel.html#module.__cached__ "module.__cached__") 的做法已被弃用。 在 Python 3.15 中，`__cached__` 将不会再被导入系统或标准库纳入考虑。 ([gh-97879](https://github.com/python/cpython/issues/97879))
       
   *   当设备 [`__spec__.parent`](../library/importlib.html#importlib.machinery.ModuleSpec.parent "importlib.machinery.ModuleSpec.parent") 失败时在模块上设置 [`__package__`](../reference/datamodel.html#module.__package__ "module.__package__") 的做法已被弃用。 在 Python 3.15 中，`__package__` 将不会再被导入系统或标准库纳入考虑。 ([gh-97879](https://github.com/python/cpython/issues/97879))
       
*   [`ctypes`](../library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python."):
   
   *   未写入文档的 `ctypes.SetPointerType()` 函数自 Python 3.13 起已被弃用。
       
*   [`http.server`](../library/http.server.html#module-http.server "http.server: HTTP server and request handlers."):
   
   *   过时且很少被使用的 [`CGIHTTPRequestHandler`](../library/http.server.html#http.server.CGIHTTPRequestHandler "http.server.CGIHTTPRequestHandler") 自 Python 3.13 起已被弃用。 不存在直接的替代品。 对于建立带有请求处理器的 Web 服务程序来说 _任何东西_ 都比 CGI 要好。
       
   *   用于 **python -m http.server** 命令行界面的 `--cgi` 旗标自 Python 3.13 起已被弃用。
       
*   [`locale`](../library/locale.html#module-locale "locale: Internationalization services."):
   
   *   [`getdefaultlocale()`](../library/locale.html#locale.getdefaultlocale "locale.getdefaultlocale") 函数自 Python 3.11 起已被弃用。 最初计划在 Python 3.13 中移除它 ([gh-90817](https://github.com/python/cpython/issues/90817))，但已被推迟至 Python 3.15。 请改用 [`getlocale()`](../library/locale.html#locale.getlocale "locale.getlocale"), [`setlocale()`](../library/locale.html#locale.setlocale "locale.setlocale") 和 [`getencoding()`](../library/locale.html#locale.getencoding "locale.getencoding")。 （由 Hugo van Kemenade 在 [gh-111187](https://github.com/python/cpython/issues/111187) 中贡献。）
       
*   [`pathlib`](../library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths"):
   
   *   [`PurePath.is_reserved()`](../library/pathlib.html#pathlib.PurePath.is_reserved "pathlib.PurePath.is_reserved") 自 Python 3.13 起已被弃用。 请使用 [`os.path.isreserved()`](../library/os.path.html#os.path.isreserved "os.path.isreserved") 来检测 Windows 上的保留路径。
       
*   [`platform`](../library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible."):
   
   *   [`java_ver()`](../library/platform.html#platform.java_ver "platform.java_ver") 自 Python 3.13 起已被弃用。 此函数仅对 Jython 支持有用，具有令人困惑的 API，并且大部分未经测试。
       
*   [`threading`](../library/threading.html#module-threading "threading: Thread-based parallelism."):
   
   *   在 Python 3.15 中 [`RLock()`](../library/threading.html#threading.RLock "threading.RLock") 将不再接受参数。 传入参数的做法自 Python 3.14 起已被弃用，因为 Python 版本不接受任何参数，而 C 版本允许任意数量的位置或关键字参数，但会忽略所有参数。
       
*   [`types`](../library/types.html#module-types "types: Names for built-in types."):
   
   *   [`types.CodeType`](../library/types.html#types.CodeType "types.CodeType"): Accessing [`co_lnotab`](../reference/datamodel.html#codeobject.co_lnotab "codeobject.co_lnotab") was deprecated in [**PEP 626**](https://peps.python.org/pep-0626/) since 3.10 and was planned to be removed in 3.12, but it only got a proper [`DeprecationWarning`](../library/exceptions.html#DeprecationWarning "DeprecationWarning") in 3.12. May be removed in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866).)
       
*   [`typing`](../library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`)."):
   
   *   The undocumented keyword argument syntax for creating [`NamedTuple`](../library/typing.html#typing.NamedTuple "typing.NamedTuple") classes (for example, `Point = NamedTuple("Point", x=int, y=int)`) has been deprecated since Python 3.13. Use the class-based syntax or the functional syntax instead.
       
   *   [`typing.no_type_check_decorator()`](../library/typing.html#typing.no_type_check_decorator "typing.no_type_check_decorator") 装饰器自 Python 3.13 起已被弃用。 存在于 [`typing`](../library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") 模块八年之后，它仍未被任何主要类型检查器所支持。
       
*   [`wave`](../library/wave.html#module-wave "wave: Provide an interface to the WAV sound format."):
   
   *   [`Wave_read`](../library/wave.html#wave.Wave_read "wave.Wave_read") 和 [`Wave_write`](../library/wave.html#wave.Wave_write "wave.Wave_write") 类的 [`getmark()`](../library/wave.html#wave.Wave_read.getmark "wave.Wave_read.getmark"), `setmark()` 和 [`getmarkers()`](../library/wave.html#wave.Wave_read.getmarkers "wave.Wave_read.getmarkers") 方法自 Python 3.13 起已被弃用。
       

### Pending removal in Python 3.16[¶](#pending-removal-in-python-3-16 "Link to this heading")

*   导入系统：
   
   *   Setting [`__loader__`](../reference/datamodel.html#module.__loader__ "module.__loader__") on a module while failing to set [`__spec__.loader`](../library/importlib.html#importlib.machinery.ModuleSpec.loader "importlib.machinery.ModuleSpec.loader") is deprecated. In Python 3.16, `__loader__` will cease to be set or taken into consideration by the import system or the standard library.
       
*   [`array`](../library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values."):
   
   *   `'u'` 格式代码 (`wchar_t`) 自 Python 3.3 起已在文档中弃用并自 Python 3.13 起在运行时弃用。 对于 Unicode 字符请改用 `'w'` 格式代码 ([`Py_UCS4`](../c-api/unicode.html#c.Py_UCS4 "Py_UCS4"))。
       
*   [`asyncio`](../library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O."):
   
   *   `asyncio.iscoroutinefunction()` is deprecated and will be removed in Python 3.16, use [`inspect.iscoroutinefunction()`](../library/inspect.html#inspect.iscoroutinefunction "inspect.iscoroutinefunction") instead. (Contributed by Jiahao Li and Kumar Aditya in [gh-122875](https://github.com/python/cpython/issues/122875).)
       
*   [`builtins`](../library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace."):
   
   *   对布尔类型 `~True` 或 `~False` 执行按位取反的操作自 Python 3.12 起已被弃用，因为它会产生奇怪和不直观的结果 (`-2` and `-1`)。 请改用 `not x` 来对布尔值执行逻辑否操作。 对于需要对下层整数执行按位取反操作的少数场合，请显式地将其转换为 `int` (`~int(x)`)。
       
*   [`shutil`](../library/shutil.html#module-shutil "shutil: High-level file operations, including copying."):
   
   *   `ExecError` 异常自 Python 3.14 起已被弃用。 它自 Python 3.4 起就未被 `shutil` 中的任何函数所使用，现在是 [`RuntimeError`](../library/exceptions.html#RuntimeError "RuntimeError") 的一个别名。
       
*   [`symtable`](../library/symtable.html#module-symtable "symtable: Interface to the compiler's internal symbol tables."):
   
   *   [`Class.get_methods`](../library/symtable.html#symtable.Class.get_methods "symtable.Class.get_methods") 方法自 Python 3.14 起被弃用。
       
*   [`sys`](../library/sys.html#module-sys "sys: Access system-specific parameters and functions."):
   
   *   [`_enablelegacywindowsfsencoding()`](../library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding") 函数自 Python 3.13 起被弃用。 请改用 [`PYTHONLEGACYWINDOWSFSENCODING`](../using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) 环境变量。
       
*   [`tarfile`](../library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files."):
   
   *   未写入文档也未被使用的 `TarFile.tarfile` 属性自 Python 3.13 起被弃用。
       

### Pending removal in future versions[¶](#pending-removal-in-future-versions "Link to this heading")

以下API将会被移除，尽管具体时间还未确定。

*   [`argparse`](../library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library."):
   
   *   Nesting argument groups and nesting mutually exclusive groups are deprecated.
       
   *   Passing the undocumented keyword argument _prefix\_chars_ to [`add_argument_group()`](../library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group") is now deprecated.
       
   *   The [`argparse.FileType`](../library/argparse.html#argparse.FileType "argparse.FileType") type converter is deprecated.
       
*   [`array`](../library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") 的 `'u'` 格式代码 ([gh-57281](https://github.com/python/cpython/issues/57281))
   
*   [`builtins`](../library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace."):
   
   *   `bool(NotImplemented)`。
       
   *   生成器: `throw(type, exc, tb)` 和 `athrow(type, exc, tb)` 签名已被弃用：请改用 `throw(exc)` 和 `athrow(exc)`，即单参数签名。
       
   *   目前 Python 接受数字类字面值后面紧跟关键字的写法，例如 `0in x`, `1or x`, `0if 1else 2`。 它允许像 `[0x1for x in y]` 这样令人困惑且有歧义的表达式 (它可以被解读为 `[0x1 for x in y]` 或者 `[0x1f or x in y]`)。 如果数字类字面值后面紧跟关键字 [`and`](../reference/expressions.html#and), [`else`](../reference/compound_stmts.html#else), [`for`](../reference/compound_stmts.html#for), [`if`](../reference/compound_stmts.html#if), [`in`](../reference/expressions.html#in), [`is`](../reference/expressions.html#is) 和 [`or`](../reference/expressions.html#or) 中的一个将会引发语法警告。 在未来的版本中它将改为语法错误。 ([gh-87999](https://github.com/python/cpython/issues/87999))
       
   *   对 `__index__()` 和 `__int__()` 方法返回非 int 类型的支持：将要求这些方法必须返回 [`int`](../library/functions.html#int "int") 的子类的实例。
       
   *   对 `__float__()` 方法返回 [`float`](../library/functions.html#float "float") 的子类的支持：将要求这些方法必须返回 [`float`](../library/functions.html#float "float") 的实例。
       
   *   对 `__complex__()` 方法返回 [`complex`](../library/functions.html#complex "complex") 的子类的支持：将要求这些方法必须返回 [`complex`](../library/functions.html#complex "complex") 的实例。
       
   *   将 `int()` 委托给 `__trunc__()` 方法。
       
   *   传入一个复数作为 [`complex()`](../library/functions.html#complex "complex") 构造器中的 _real_ 或 _imag_ 参数的做法现在已被弃用；它应当仅作为单个位置参数被传入。 （由 Serhiy Storchaka 在 [gh-109218](https://github.com/python/cpython/issues/109218) 中贡献。）.)
       
*   [`calendar`](../library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program."): `calendar.January` 和 `calendar.February` 常量已被弃用并由 [`calendar.JANUARY`](../library/calendar.html#calendar.JANUARY "calendar.JANUARY") 和 [`calendar.FEBRUARY`](../library/calendar.html#calendar.FEBRUARY "calendar.FEBRUARY") 替代。 （由 Prince Roshan 在 [gh-103636](https://github.com/python/cpython/issues/103636) 中贡献。）
   
*   [`codeobject.co_lnotab`](../reference/datamodel.html#codeobject.co_lnotab "codeobject.co_lnotab"): 改用 [`codeobject.co_lines()`](../reference/datamodel.html#codeobject.co_lines "codeobject.co_lines") 方法。
   
*   [`datetime`](../library/datetime.html#module-datetime "datetime: Basic date and time types."):
   
   *   [`utcnow()`](../library/datetime.html#datetime.datetime.utcnow "datetime.datetime.utcnow"): 使用 `datetime.datetime.now(tz=datetime.UTC)`。
       
   *   [`utcfromtimestamp()`](../library/datetime.html#datetime.datetime.utcfromtimestamp "datetime.datetime.utcfromtimestamp"): 使用 `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`。
       
*   [`gettext`](../library/gettext.html#module-gettext "gettext: Multilingual internationalization services."): 复数值必须是一个整数。
   
*   [`importlib`](../library/importlib.html#module-importlib "importlib: The implementation of the import machinery."):
   
   *   `load_module()` 方法：改用 `exec_module()`。
       
   *   [`cache_from_source()`](../library/importlib.html#importlib.util.cache_from_source "importlib.util.cache_from_source") _debug\_override_ 形参已被弃用：改用 _optimization_ 形能耐。
       
*   [`importlib.metadata`](../library/importlib.metadata.html#module-importlib.metadata "importlib.metadata: Accessing package metadata"):
   
   *   `EntryPoints` 元组接口。
       
   *   返回值中隐式的 `None`。
       
*   [`logging`](../library/logging.html#module-logging "logging: Flexible event logging system for applications."): `warn()` 方法自 Python 3.3 起已被弃用，请改用 [`warning()`](../library/logging.html#logging.warning "logging.warning")。
   
*   [`mailbox`](../library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats"): 对 StringIO 输入和文本模式的使用已被弃用，改用 BytesIO 和二进制模式。
   
*   [`os`](../library/os.html#module-os "os: Miscellaneous operating system interfaces."): 在多线程的进程中调用 [`os.register_at_fork()`](../library/os.html#os.register_at_fork "os.register_at_fork")。
   
*   `pydoc.ErrorDuringImport`: 使用元组值作为 _exc\_info_ 形参的做法已被弃用，应使用异常实例。
   
*   [`re`](../library/re.html#module-re "re: Regular expression operations."): 现在对于正则表达式中的数字分组引用和分组名称将应用更严格的规则。 现在只接受 ASCII 数字序列作为数字引用。 字节串模式和替换字符串中的分组名称现在只能包含 ASCII 字母和数字以及下划线。 （由 Serhiy Storchaka 在 [gh-91760](https://github.com/python/cpython/issues/91760) 中贡献。）
   
*   `sre_compile`, `sre_constants` 和 `sre_parse` 模块。
   
*   [`shutil`](../library/shutil.html#module-shutil "shutil: High-level file operations, including copying."): [`rmtree()`](../library/shutil.html#shutil.rmtree "shutil.rmtree") 的 _onerror_ 形参在 Python 3.12 中已被弃用；请改用 _onexc_ 形参。
   
*   [`ssl`](../library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects") 选项和协议：
   
   *   [`ssl.SSLContext`](../library/ssl.html#ssl.SSLContext "ssl.SSLContext") 不带 protocol 参数的做法已被弃用。
       
   *   [`ssl.SSLContext`](../library/ssl.html#ssl.SSLContext "ssl.SSLContext"): [`set_npn_protocols()`](../library/ssl.html#ssl.SSLContext.set_npn_protocols "ssl.SSLContext.set_npn_protocols") 和 `selected_npn_protocol()` 已被弃用：请改用 ALPN.
       
   *   `ssl.OP_NO_SSL*` 选项
       
   *   `ssl.OP_NO_TLS*` 选项
       
   *   `ssl.PROTOCOL_SSLv3`
       
   *   `ssl.PROTOCOL_TLS`
       
   *   `ssl.PROTOCOL_TLSv1`
       
   *   `ssl.PROTOCOL_TLSv1_1`
       
   *   `ssl.PROTOCOL_TLSv1_2`
       
   *   `ssl.TLSVersion.SSLv3`
       
   *   `ssl.TLSVersion.TLSv1`
       
   *   `ssl.TLSVersion.TLSv1_1`
       
*   [`sysconfig.is_python_build()`](../library/sysconfig.html#sysconfig.is_python_build "sysconfig.is_python_build") _check\_home_ 形参已被弃用并会被忽略。
   
*   [`threading`](../library/threading.html#module-threading "threading: Thread-based parallelism.") 的方法：
   
   *   `threading.Condition.notifyAll()`: 使用 [`notify_all()`](../library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all")。
       
   *   `threading.Event.isSet()`: 使用 [`is_set()`](../library/threading.html#threading.Event.is_set "threading.Event.is_set")。
       
   *   `threading.Thread.isDaemon()`, [`threading.Thread.setDaemon()`](../library/threading.html#threading.Thread.setDaemon "threading.Thread.setDaemon"): 使用 [`threading.Thread.daemon`](../library/threading.html#threading.Thread.daemon "threading.Thread.daemon") 属性。
       
   *   `threading.Thread.getName()`, [`threading.Thread.setName()`](../library/threading.html#threading.Thread.setName "threading.Thread.setName"): 使用 [`threading.Thread.name`](../library/threading.html#threading.Thread.name "threading.Thread.name") 属性。
       
   *   `threading.currentThread()`: 使用 [`threading.current_thread()`](../library/threading.html#threading.current_thread "threading.current_thread")。
       
   *   `threading.activeCount()`: 使用 [`threading.active_count()`](../library/threading.html#threading.active_count "threading.active_count")。
       
*   [`typing.Text`](../library/typing.html#typing.Text "typing.Text") ([gh-92332](https://github.com/python/cpython/issues/92332))。
   
*   [`unittest.IsolatedAsyncioTestCase`](../library/unittest.html#unittest.IsolatedAsyncioTestCase "unittest.IsolatedAsyncioTestCase"): 从测试用例返回不为 `None` 的值的做法已被弃用。
   
*   [`urllib.parse`](../library/urllib.parse.html#module-urllib.parse "urllib.parse: Parse URLs into or assemble them from components.") 函数已被弃用：改用 [`urlparse()`](../library/urllib.parse.html#urllib.parse.urlparse "urllib.parse.urlparse")
   
   *   `splitattr()`
       
   *   `splithost()`
       
   *   `splitnport()`
       
   *   `splitpasswd()`
       
   *   `splitport()`
       
   *   `splitquery()`
       
   *   `splittag()`
       
   *   `splittype()`
       
   *   `splituser()`
       
   *   `splitvalue()`
       
   *   `to_bytes()`
       
*   [`urllib.request`](../library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs."): 发起请求的 [`URLopener`](../library/urllib.request.html#urllib.request.URLopener "urllib.request.URLopener") 和 [`FancyURLopener`](../library/urllib.request.html#urllib.request.FancyURLopener "urllib.request.FancyURLopener") 方式已被弃用。 改用更新 [`urlopen()`](../library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") 函数和方法。
   
*   [`wsgiref`](../library/wsgiref.html#module-wsgiref "wsgiref: WSGI Utilities and Reference Implementation."): `SimpleHandler.stdout.write()` 不应执行部分写入。
   
*   [`xml.etree.ElementTree`](../library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API."): 对 [`Element`](../library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") 的真值测试已被弃用。 在未来的发布版中它将始终返回 `True`。 建议改用显式的 `len(elem)` 或 `elem is not None` 测试。
   
*   [`zipimport.zipimporter.load_module()`](../library/zipimport.html#zipimport.zipimporter.load_module "zipimport.zipimporter.load_module") 已被弃用：请改用 [`exec_module()`](../library/zipimport.html#zipimport.zipimporter.exec_module "zipimport.zipimporter.exec_module")。
   

CPython 字节码的变化[¶](#cpython-bytecode-changes "Link to this heading")
-------------------------------------------------------------------

*   The oparg of [`YIELD_VALUE`](../library/dis.html#opcode-YIELD_VALUE) is now `1` if the yield is part of a yield-from or await, and `0` otherwise. The oparg of [`RESUME`](../library/dis.html#opcode-RESUME) was changed to add a bit indicating if the except-depth is 1, which is needed to optimize closing of generators. (Contributed by Irit Katriel in [gh-111354](https://github.com/python/cpython/issues/111354).)
   

C API 的变化[¶](#c-api-changes "Link to this heading")
---------------------------------------------------

### 新的特性[¶](#id7 "Link to this heading")

*   增加 [PyMonitoring C API](../c-api/monitoring.html#c-api-monitoring) 用于生成 [**PEP 669**](https://peps.python.org/pep-0669/) 监控事件：
   
   *   [`PyMonitoringState`](../c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
       
   *   [`PyMonitoring_FirePyStartEvent()`](../c-api/monitoring.html#c.PyMonitoring_FirePyStartEvent "PyMonitoring_FirePyStartEvent")
       
   *   [`PyMonitoring_FirePyResumeEvent()`](../c-api/monitoring.html#c.PyMonitoring_FirePyResumeEvent "PyMonitoring_FirePyResumeEvent")
       
   *   [`PyMonitoring_FirePyReturnEvent()`](../c-api/monitoring.html#c.PyMonitoring_FirePyReturnEvent "PyMonitoring_FirePyReturnEvent")
       
   *   [`PyMonitoring_FirePyYieldEvent()`](../c-api/monitoring.html#c.PyMonitoring_FirePyYieldEvent "PyMonitoring_FirePyYieldEvent")
       
   *   [`PyMonitoring_FireCallEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireCallEvent "PyMonitoring_FireCallEvent")
       
   *   [`PyMonitoring_FireLineEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireLineEvent "PyMonitoring_FireLineEvent")
       
   *   [`PyMonitoring_FireJumpEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireJumpEvent "PyMonitoring_FireJumpEvent")
       
   *   [`PyMonitoring_FireBranchEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireBranchEvent "PyMonitoring_FireBranchEvent")
       
   *   [`PyMonitoring_FireCReturnEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireCReturnEvent "PyMonitoring_FireCReturnEvent")
       
   *   [`PyMonitoring_FirePyThrowEvent()`](../c-api/monitoring.html#c.PyMonitoring_FirePyThrowEvent "PyMonitoring_FirePyThrowEvent")
       
   *   [`PyMonitoring_FireRaiseEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireRaiseEvent "PyMonitoring_FireRaiseEvent")
       
   *   [`PyMonitoring_FireCRaiseEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireCRaiseEvent "PyMonitoring_FireCRaiseEvent")
       
   *   [`PyMonitoring_FireReraiseEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireReraiseEvent "PyMonitoring_FireReraiseEvent")
       
   *   [`PyMonitoring_FireExceptionHandledEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireExceptionHandledEvent "PyMonitoring_FireExceptionHandledEvent")
       
   *   [`PyMonitoring_FirePyUnwindEvent()`](../c-api/monitoring.html#c.PyMonitoring_FirePyUnwindEvent "PyMonitoring_FirePyUnwindEvent")
       
   *   [`PyMonitoring_FireStopIterationEvent()`](../c-api/monitoring.html#c.PyMonitoring_FireStopIterationEvent "PyMonitoring_FireStopIterationEvent")
       
   *   [`PyMonitoring_EnterScope()`](../c-api/monitoring.html#c.PyMonitoring_EnterScope "PyMonitoring_EnterScope")
       
   *   [`PyMonitoring_ExitScope()`](../c-api/monitoring.html#c.PyMonitoring_ExitScope "PyMonitoring_ExitScope")
       
   
   （由 Irit Katriel 在 [gh-111997](https://github.com/python/cpython/issues/111997) 中贡献。）
   
*   增加了 [`PyMutex`](../c-api/init.html#c.PyMutex "PyMutex")，它是占用一个字节的轻量级互斥锁，以及新的 [`PyMutex_Lock()`](../c-api/init.html#c.PyMutex_Lock "PyMutex_Lock") 和 [`PyMutex_Unlock()`](../c-api/init.html#c.PyMutex_Unlock "PyMutex_Unlock") 函数。 如果操作需要阻塞则 `PyMutex_Lock()` 将释放 (当前持有的) [GIL](../glossary.html#term-GIL)。 （由 Sam Gross 在 [gh-108724](https://github.com/python/cpython/issues/108724) 中贡献。）
   
*   增加了 [PyTime C API](../c-api/time.html#c-api-time) 以提供对系统时钟的访问：
   
   *   [`PyTime_t`](../c-api/time.html#c.PyTime_t "PyTime_t")。
       
   *   [`PyTime_MIN`](../c-api/time.html#c.PyTime_MIN "PyTime_MIN") 和 [`PyTime_MAX`](../c-api/time.html#c.PyTime_MAX "PyTime_MAX")。
       
   *   [`PyTime_AsSecondsDouble()`](../c-api/time.html#c.PyTime_AsSecondsDouble "PyTime_AsSecondsDouble")。
       
   *   [`PyTime_Monotonic()`](../c-api/time.html#c.PyTime_Monotonic "PyTime_Monotonic")。
       
   *   [`PyTime_MonotonicRaw()`](../c-api/time.html#c.PyTime_MonotonicRaw "PyTime_MonotonicRaw")。
       
   *   [`PyTime_PerfCounter()`](../c-api/time.html#c.PyTime_PerfCounter "PyTime_PerfCounter")。
       
   *   [`PyTime_PerfCounterRaw()`](../c-api/time.html#c.PyTime_PerfCounterRaw "PyTime_PerfCounterRaw")。
       
   *   [`PyTime_Time()`](../c-api/time.html#c.PyTime_Time "PyTime_Time")。
       
   *   [`PyTime_TimeRaw()`](../c-api/time.html#c.PyTime_TimeRaw "PyTime_TimeRaw")。
       
   
   （由 Victor Stinner 和 Petr Viktorin 在 [gh-110850](https://github.com/python/cpython/issues/110850) 中贡献。）
   
*   Add the [`PyDict_ContainsString()`](../c-api/dict.html#c.PyDict_ContainsString "PyDict_ContainsString") function with the same behavior as [`PyDict_Contains()`](../c-api/dict.html#c.PyDict_Contains "PyDict_Contains"), but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](../c-api/structures.html#c.PyObject "PyObject")\*. (Contributed by Victor Stinner in [gh-108314](https://github.com/python/cpython/issues/108314).)
   
*   Add the [`PyDict_GetItemRef()`](../c-api/dict.html#c.PyDict_GetItemRef "PyDict_GetItemRef") and [`PyDict_GetItemStringRef()`](../c-api/dict.html#c.PyDict_GetItemStringRef "PyDict_GetItemStringRef") functions, which behave similarly to [`PyDict_GetItemWithError()`](../c-api/dict.html#c.PyDict_GetItemWithError "PyDict_GetItemWithError"), but return a [strong reference](../glossary.html#term-strong-reference) instead of a [borrowed reference](../glossary.html#term-borrowed-reference). Moreover, these functions return `-1` on error, removing the need to check `PyErr_Occurred()`. (Contributed by Victor Stinner in [gh-106004](https://github.com/python/cpython/issues/106004).)
   
*   Add the [`PyDict_SetDefaultRef()`](../c-api/dict.html#c.PyDict_SetDefaultRef "PyDict_SetDefaultRef") function, which behaves similarly to [`PyDict_SetDefault()`](../c-api/dict.html#c.PyDict_SetDefault "PyDict_SetDefault"), but returns a [strong reference](../glossary.html#term-strong-reference) instead of a [borrowed reference](../glossary.html#term-borrowed-reference). This function returns `-1` on error, `0` on insertion, and `1` if the key was already present in the dictionary. (Contributed by Sam Gross in [gh-112066](https://github.com/python/cpython/issues/112066).)
   
*   Add the [`PyDict_Pop()`](../c-api/dict.html#c.PyDict_Pop "PyDict_Pop") and [`PyDict_PopString()`](../c-api/dict.html#c.PyDict_PopString "PyDict_PopString") functions to remove a key from a dictionary and optionally return the removed value. This is similar to [`dict.pop()`](../library/stdtypes.html#dict.pop "dict.pop"), though there is no default value, and [`KeyError`](../library/exceptions.html#KeyError "KeyError") is not raised for missing keys. (Contributed by Stefan Behnel and Victor Stinner in [gh-111262](https://github.com/python/cpython/issues/111262).)
   
*   Add the [`PyMapping_GetOptionalItem()`](../c-api/mapping.html#c.PyMapping_GetOptionalItem "PyMapping_GetOptionalItem") and [`PyMapping_GetOptionalItemString()`](../c-api/mapping.html#c.PyMapping_GetOptionalItemString "PyMapping_GetOptionalItemString") functions as alternatives to [`PyObject_GetItem()`](../c-api/object.html#c.PyObject_GetItem "PyObject_GetItem") and [`PyMapping_GetItemString()`](../c-api/mapping.html#c.PyMapping_GetItemString "PyMapping_GetItemString") respectively. The new functions do not raise [`KeyError`](../library/exceptions.html#KeyError "KeyError") if the requested key is missing from the mapping. These variants are more convenient and faster if a missing key should not be treated as a failure. (Contributed by Serhiy Storchaka in [gh-106307](https://github.com/python/cpython/issues/106307).)
   
*   Add the [`PyObject_GetOptionalAttr()`](../c-api/object.html#c.PyObject_GetOptionalAttr "PyObject_GetOptionalAttr") and [`PyObject_GetOptionalAttrString()`](../c-api/object.html#c.PyObject_GetOptionalAttrString "PyObject_GetOptionalAttrString") functions as alternatives to [`PyObject_GetAttr()`](../c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr") and [`PyObject_GetAttrString()`](../c-api/object.html#c.PyObject_GetAttrString "PyObject_GetAttrString") respectively. The new functions do not raise [`AttributeError`](../library/exceptions.html#AttributeError "AttributeError") if the requested attribute is not found on the object. These variants are more convenient and faster if the missing attribute should not be treated as a failure. (Contributed by Serhiy Storchaka in [gh-106521](https://github.com/python/cpython/issues/106521).)
   
*   Add the [`PyErr_FormatUnraisable()`](../c-api/exceptions.html#c.PyErr_FormatUnraisable "PyErr_FormatUnraisable") function as an extension to [`PyErr_WriteUnraisable()`](../c-api/exceptions.html#c.PyErr_WriteUnraisable "PyErr_WriteUnraisable") that allows customizing the warning message. (Contributed by Serhiy Storchaka in [gh-108082](https://github.com/python/cpython/issues/108082).)
   
*   Add new functions that return a [strong reference](../glossary.html#term-strong-reference) instead of a [borrowed reference](../glossary.html#term-borrowed-reference) for frame locals, globals, and builtins, as part of [PEP 667](#whatsnew313-locals-semantics):
   
   *   [`PyEval_GetFrameBuiltins()`](../c-api/reflection.html#c.PyEval_GetFrameBuiltins "PyEval_GetFrameBuiltins") replaces [`PyEval_GetBuiltins()`](../c-api/reflection.html#c.PyEval_GetBuiltins "PyEval_GetBuiltins")
       
   *   [`PyEval_GetFrameGlobals()`](../c-api/reflection.html#c.PyEval_GetFrameGlobals "PyEval_GetFrameGlobals") replaces [`PyEval_GetGlobals()`](../c-api/reflection.html#c.PyEval_GetGlobals "PyEval_GetGlobals")
       
   *   [`PyEval_GetFrameLocals()`](../c-api/reflection.html#c.PyEval_GetFrameLocals "PyEval_GetFrameLocals") replaces [`PyEval_GetLocals()`](../c-api/reflection.html#c.PyEval_GetLocals "PyEval_GetLocals")
       
   
   (Contributed by Mark Shannon and Tian Gao in [gh-74929](https://github.com/python/cpython/issues/74929).)
   
*   Add the [`Py_GetConstant()`](../c-api/object.html#c.Py_GetConstant "Py_GetConstant") and [`Py_GetConstantBorrowed()`](../c-api/object.html#c.Py_GetConstantBorrowed "Py_GetConstantBorrowed") functions to get [strong](../glossary.html#term-strong-reference) or [borrowed](../glossary.html#term-borrowed-reference) references to constants. For example, `Py_GetConstant(Py_CONSTANT_ZERO)` returns a strong reference to the constant zero. (Contributed by Victor Stinner in [gh-115754](https://github.com/python/cpython/issues/115754).)
   
*   Add the [`PyImport_AddModuleRef()`](../c-api/import.html#c.PyImport_AddModuleRef "PyImport_AddModuleRef") function as a replacement for [`PyImport_AddModule()`](../c-api/import.html#c.PyImport_AddModule "PyImport_AddModule") that returns a [strong reference](../glossary.html#term-strong-reference) instead of a [borrowed reference](../glossary.html#term-borrowed-reference). (Contributed by Victor Stinner in [gh-105922](https://github.com/python/cpython/issues/105922).)
   
*   Add the [`Py_IsFinalizing()`](../c-api/init.html#c.Py_IsFinalizing "Py_IsFinalizing") function to check whether the main Python interpreter is [shutting down](../glossary.html#term-interpreter-shutdown). (Contributed by Victor Stinner in [gh-108014](https://github.com/python/cpython/issues/108014).)
   
*   Add the [`PyList_GetItemRef()`](../c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef") function as a replacement for [`PyList_GetItem()`](../c-api/list.html#c.PyList_GetItem "PyList_GetItem") that returns a [strong reference](../glossary.html#term-strong-reference) instead of a [borrowed reference](../glossary.html#term-borrowed-reference). (Contributed by Sam Gross in [gh-114329](https://github.com/python/cpython/issues/114329).)
   
*   Add the [`PyList_Extend()`](../c-api/list.html#c.PyList_Extend "PyList_Extend") and [`PyList_Clear()`](../c-api/list.html#c.PyList_Clear "PyList_Clear") functions, mirroring the Python `list.extend()` and `list.clear()` methods. (Contributed by Victor Stinner in [gh-111138](https://github.com/python/cpython/issues/111138).)
   
*   Add the [`PyLong_AsInt()`](../c-api/long.html#c.PyLong_AsInt "PyLong_AsInt") function. It behaves similarly to [`PyLong_AsLong()`](../c-api/long.html#c.PyLong_AsLong "PyLong_AsLong"), but stores the result in a C int instead of a C long. (Contributed by Victor Stinner in [gh-108014](https://github.com/python/cpython/issues/108014).)
   
*   Add the [`PyLong_AsNativeBytes()`](../c-api/long.html#c.PyLong_AsNativeBytes "PyLong_AsNativeBytes"), [`PyLong_FromNativeBytes()`](../c-api/long.html#c.PyLong_FromNativeBytes "PyLong_FromNativeBytes"), and [`PyLong_FromUnsignedNativeBytes()`](../c-api/long.html#c.PyLong_FromUnsignedNativeBytes "PyLong_FromUnsignedNativeBytes") functions to simplify converting between native integer types and Python [`int`](../library/functions.html#int "int") objects. (Contributed by Steve Dower in [gh-111140](https://github.com/python/cpython/issues/111140).)
   
*   Add [`PyModule_Add()`](../c-api/module.html#c.PyModule_Add "PyModule_Add") function, which is similar to [`PyModule_AddObjectRef()`](../c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef") and [`PyModule_AddObject()`](../c-api/module.html#c.PyModule_AddObject "PyModule_AddObject"), but always steals a reference to the value. (Contributed by Serhiy Storchaka in [gh-86493](https://github.com/python/cpython/issues/86493).)
   
*   Add the [`PyObject_GenericHash()`](../c-api/hash.html#c.PyObject_GenericHash "PyObject_GenericHash") function that implements the default hashing function of a Python object. (Contributed by Serhiy Storchaka in [gh-113024](https://github.com/python/cpython/issues/113024).)
   
*   Add the [`Py_HashPointer()`](../c-api/hash.html#c.Py_HashPointer "Py_HashPointer") function to hash a raw pointer. (Contributed by Victor Stinner in [gh-111545](https://github.com/python/cpython/issues/111545).)
   
*   Add the [`PyObject_VisitManagedDict()`](../c-api/object.html#c.PyObject_VisitManagedDict "PyObject_VisitManagedDict") and [`PyObject_ClearManagedDict()`](../c-api/object.html#c.PyObject_ClearManagedDict "PyObject_ClearManagedDict") functions. which must be called by the traverse and clear functions of a type using the [`Py_TPFLAGS_MANAGED_DICT`](../c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT") flag. The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/) can be used to use these functions with Python 3.11 and 3.12. (Contributed by Victor Stinner in [gh-107073](https://github.com/python/cpython/issues/107073).)
   
*   Add the [`PyRefTracer_SetTracer()`](../c-api/init.html#c.PyRefTracer_SetTracer "PyRefTracer_SetTracer") and [`PyRefTracer_GetTracer()`](../c-api/init.html#c.PyRefTracer_GetTracer "PyRefTracer_GetTracer") functions, which enable tracking object creation and destruction in the same way that the [`tracemalloc`](../library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.") module does. (Contributed by Pablo Galindo in [gh-93502](https://github.com/python/cpython/issues/93502).)
   
*   Add the [`PySys_AuditTuple()`](../c-api/sys.html#c.PySys_AuditTuple "PySys_AuditTuple") function as an alternative to [`PySys_Audit()`](../c-api/sys.html#c.PySys_Audit "PySys_Audit") that takes event arguments as a Python [`tuple`](../library/stdtypes.html#tuple "tuple") object. (Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283).)
   
*   Add the [`PyThreadState_GetUnchecked()`](../c-api/init.html#c.PyThreadState_GetUnchecked "PyThreadState_GetUnchecked") function as an alternative to [`PyThreadState_Get()`](../c-api/init.html#c.PyThreadState_Get "PyThreadState_Get") that doesn't kill the process with a fatal error if it is `NULL`. The caller is responsible for checking if the result is `NULL`. (Contributed by Victor Stinner in [gh-108867](https://github.com/python/cpython/issues/108867).)
   
*   Add the [`PyType_GetFullyQualifiedName()`](../c-api/type.html#c.PyType_GetFullyQualifiedName "PyType_GetFullyQualifiedName") function to get the type's fully qualified name. The module name is prepended if [`type.__module__`](../reference/datamodel.html#type.__module__ "type.__module__") is a string and is not equal to either `'builtins'` or `'__main__'`. (Contributed by Victor Stinner in [gh-111696](https://github.com/python/cpython/issues/111696).)
   
*   Add the [`PyType_GetModuleName()`](../c-api/type.html#c.PyType_GetModuleName "PyType_GetModuleName") function to get the type's module name. This is equivalent to getting the [`type.__module__`](../reference/datamodel.html#type.__module__ "type.__module__") attribute. (Contributed by Eric Snow and Victor Stinner in [gh-111696](https://github.com/python/cpython/issues/111696).)
   
*   Add the [`PyUnicode_EqualToUTF8AndSize()`](../c-api/unicode.html#c.PyUnicode_EqualToUTF8AndSize "PyUnicode_EqualToUTF8AndSize") and [`PyUnicode_EqualToUTF8()`](../c-api/unicode.html#c.PyUnicode_EqualToUTF8 "PyUnicode_EqualToUTF8") functions to compare a Unicode object with a const char\* UTF-8 encoded string and `1` if they are equal or `0` otherwise. These functions do not raise exceptions. (Contributed by Serhiy Storchaka in [gh-110289](https://github.com/python/cpython/issues/110289).)
   
*   增加 [`PyWeakref_GetRef()`](../c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef") 函数作为 [`PyWeakref_GetObject()`](../c-api/weakref.html#c.PyWeakref_GetObject "PyWeakref_GetObject") 的替代，它将返回一个 [strong reference](../glossary.html#term-strong-reference) 或是在引用对象不再存活时返回 `NULL`。 （由 Victor Stinner 在 [gh-105927](https://github.com/python/cpython/issues/105927) 中贡献。）
   
*   增加了静默地忽略错误的函数的已修正变体形式：
   
   *   [`PyObject_HasAttrWithError()`](../c-api/object.html#c.PyObject_HasAttrWithError "PyObject_HasAttrWithError") 替代 [`PyObject_HasAttr()`](../c-api/object.html#c.PyObject_HasAttr "PyObject_HasAttr")。
       
   *   [`PyObject_HasAttrStringWithError()`](../c-api/object.html#c.PyObject_HasAttrStringWithError "PyObject_HasAttrStringWithError") 替代 [`PyObject_HasAttrString()`](../c-api/object.html#c.PyObject_HasAttrString "PyObject_HasAttrString")。
       
   *   [`PyMapping_HasKeyWithError()`](../c-api/mapping.html#c.PyMapping_HasKeyWithError "PyMapping_HasKeyWithError") 替代 [`PyMapping_HasKey()`](../c-api/mapping.html#c.PyMapping_HasKey "PyMapping_HasKey")。
       
   *   [`PyMapping_HasKeyStringWithError()`](../c-api/mapping.html#c.PyMapping_HasKeyStringWithError "PyMapping_HasKeyStringWithError") 替代 [`PyMapping_HasKeyString()`](../c-api/mapping.html#c.PyMapping_HasKeyString "PyMapping_HasKeyString")。
       
   
   这些新函数将返回 `-1` 表示错误而返回标准的 `1` 表示真值以及 `0` 表示假值。
   
   （由 Serhiy Storchaka 在 [gh-108511](https://github.com/python/cpython/issues/108511) 中贡献。）
   

### 被改变的 C API[¶](#changed-c-apis "Link to this heading")

*   The _keywords_ parameter of [`PyArg_ParseTupleAndKeywords()`](../c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords") and [`PyArg_VaParseTupleAndKeywords()`](../c-api/arg.html#c.PyArg_VaParseTupleAndKeywords "PyArg_VaParseTupleAndKeywords") now has type char \*const\* in C and const char \*const\* in C++, instead of char\*\*. In C++, this makes these functions compatible with arguments of type const char \*const\*, const char\*\*, or char \*const\* without an explicit type cast. In C, the functions only support arguments of type char \*const\*. This can be overridden with the [`PY_CXX_CONST`](../c-api/arg.html#c.PY_CXX_CONST "PY_CXX_CONST") macro. (Contributed by Serhiy Storchaka in [gh-65210](https://github.com/python/cpython/issues/65210).)
   
*   [`PyArg_ParseTupleAndKeywords()`](../c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords") now supports non-ASCII keyword parameter names. (Contributed by Serhiy Storchaka in [gh-110815](https://github.com/python/cpython/issues/110815).)
   
*   The `PyCode_GetFirstFree()` function is now unstable API and is now named [`PyUnstable_Code_GetFirstFree()`](../c-api/code.html#c.PyUnstable_Code_GetFirstFree "PyUnstable_Code_GetFirstFree"). (Contributed by Bogdan Romanyuk in [gh-115781](https://github.com/python/cpython/issues/115781).)
   
*   The [`PyDict_GetItem()`](../c-api/dict.html#c.PyDict_GetItem "PyDict_GetItem"), [`PyDict_GetItemString()`](../c-api/dict.html#c.PyDict_GetItemString "PyDict_GetItemString"), [`PyMapping_HasKey()`](../c-api/mapping.html#c.PyMapping_HasKey "PyMapping_HasKey"), [`PyMapping_HasKeyString()`](../c-api/mapping.html#c.PyMapping_HasKeyString "PyMapping_HasKeyString"), [`PyObject_HasAttr()`](../c-api/object.html#c.PyObject_HasAttr "PyObject_HasAttr"), [`PyObject_HasAttrString()`](../c-api/object.html#c.PyObject_HasAttrString "PyObject_HasAttrString"), and [`PySys_GetObject()`](../c-api/sys.html#c.PySys_GetObject "PySys_GetObject") functions, each of which clears all errors which occurred when calling them now reports these errors using [`sys.unraisablehook()`](../library/sys.html#sys.unraisablehook "sys.unraisablehook"). You may replace them with other functions as recommended in the documentation. (Contributed by Serhiy Storchaka in [gh-106672](https://github.com/python/cpython/issues/106672).)
   
*   Add support for the `%T`, `%#T`, `%N` and `%#N` formats to [`PyUnicode_FromFormat()`](../c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat"):
   
   *   `%T`: Get the fully qualified name of an object type
       
   *   `%#T`: As above, but use a colon as the separator
       
   *   `%N`: Get the fully qualified name of a type
       
   *   `%#N`: As above, but use a colon as the separator
       
   
   See [**PEP 737**](https://peps.python.org/pep-0737/) for more information. (Contributed by Victor Stinner in [gh-111696](https://github.com/python/cpython/issues/111696).)
   
*   You no longer have to define the `PY_SSIZE_T_CLEAN` macro before including `Python.h` when using `#` formats in [format codes](../c-api/arg.html#arg-parsing-string-and-buffers). APIs accepting the format codes always use `Py_ssize_t` for `#` formats. (Contributed by Inada Naoki in [gh-104922](https://github.com/python/cpython/issues/104922).)
   
*   如果 Python 是使用 [调试模式](../using/configure.html#debug-build) 或 [`附带断言`](../using/configure.html#cmdoption-with-assertions) 构建的，[`PyTuple_SET_ITEM()`](../c-api/tuple.html#c.PyTuple_SET_ITEM "PyTuple_SET_ITEM") 和 [`PyList_SET_ITEM()`](../c-api/list.html#c.PyList_SET_ITEM "PyList_SET_ITEM") 现在将通过一个断言来检查 index 参数。 （由 Victor Stinner 在 [gh-106168](https://github.com/python/cpython/issues/106168) 中贡献。）
   

### 受限 C API 的改变[¶](#limited-c-api-changes "Link to this heading")

*   下列函数现在被包括在受限 C API 中：
   
   *   [`PyMem_RawMalloc()`](../c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
       
   *   [`PyMem_RawCalloc()`](../c-api/memory.html#c.PyMem_RawCalloc "PyMem_RawCalloc")
       
   *   [`PyMem_RawRealloc()`](../c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
       
   *   [`PyMem_RawFree()`](../c-api/memory.html#c.PyMem_RawFree "PyMem_RawFree")
       
   *   [`PySys_Audit()`](../c-api/sys.html#c.PySys_Audit "PySys_Audit")
       
   *   [`PySys_AuditTuple()`](../c-api/sys.html#c.PySys_AuditTuple "PySys_AuditTuple")
       
   *   [`PyType_GetModuleByDef()`](../c-api/type.html#c.PyType_GetModuleByDef "PyType_GetModuleByDef")
       
   
   （由 Victor Stinner 在 [gh-85283](https://github.com/python/cpython/issues/85283), [gh-85283](https://github.com/python/cpython/issues/85283) 和 [gh-116936](https://github.com/python/cpython/issues/116936) 中贡献。）
   
*   使用 [`--with-trace-refs`](../using/configure.html#cmdoption-with-trace-refs) (跟踪引用) 构建的 Python 现在支持 [受限 API](../c-api/stable.html#limited-c-api)。 （由 Victor Stinner 在 [gh-108634](https://github.com/python/cpython/issues/108634) 中贡献。）
   

### Removed C APIs[¶](#removed-c-apis "Link to this heading")

*   Remove several functions, macros, variables, etc with names prefixed by `_Py` or `_PY` (which are considered private). If your project is affected by one of these removals and you believe that the removed API should remain available, please [open a new issue](../bugs.html#using-the-tracker) to request a public C API and add `cc: @vstinner` to the issue to notify Victor Stinner. (Contributed by Victor Stinner in [gh-106320](https://github.com/python/cpython/issues/106320).)
   
*   Remove old buffer protocols deprecated in Python 3.0. Use [缓冲协议](../c-api/buffer.html#bufferobjects) instead.
   
   *   `PyObject_CheckReadBuffer()`: Use [`PyObject_CheckBuffer()`](../c-api/buffer.html#c.PyObject_CheckBuffer "PyObject_CheckBuffer") to test whether the object supports the buffer protocol. Note that [`PyObject_CheckBuffer()`](../c-api/buffer.html#c.PyObject_CheckBuffer "PyObject_CheckBuffer") doesn't guarantee that [`PyObject_GetBuffer()`](../c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer") will succeed. To test if the object is actually readable, see the next example of [`PyObject_GetBuffer()`](../c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer").
       
   *   `PyObject_AsCharBuffer()`, `PyObject_AsReadBuffer()`: Use [`PyObject_GetBuffer()`](../c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer") and [`PyBuffer_Release()`](../c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release") instead:
       
       Py\_buffer view;
       if (PyObject\_GetBuffer(obj, &view, PyBUF\_SIMPLE) < 0) {
           return NULL;
       }
       // Use \`view.buf\` and \`view.len\` to read from the buffer.
       // You may need to cast buf as \`(const char\*)view.buf\`.
       PyBuffer\_Release(&view);
       
   *   `PyObject_AsWriteBuffer()`: Use [`PyObject_GetBuffer()`](../c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer") and [`PyBuffer_Release()`](../c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release") instead:
       
       Py\_buffer view;
       if (PyObject\_GetBuffer(obj, &view, PyBUF\_WRITABLE) < 0) {
           return NULL;
       }
       // Use \`view.buf\` and \`view.len\` to write to the buffer.
       PyBuffer\_Release(&view);
       
   
   (Contributed by Inada Naoki in [gh-85275](https://github.com/python/cpython/issues/85275).)
   
*   删除了在 Python 3.9 中弃用的各种函数：
   
   *   `PyEval_CallObject()`, `PyEval_CallObjectWithKeywords()`: Use [`PyObject_CallNoArgs()`](../c-api/call.html#c.PyObject_CallNoArgs "PyObject_CallNoArgs") or [`PyObject_Call()`](../c-api/call.html#c.PyObject_Call "PyObject_Call") instead.
       
       警告
       
       In [`PyObject_Call()`](../c-api/call.html#c.PyObject_Call "PyObject_Call"), positional arguments must be a [`tuple`](../library/stdtypes.html#tuple "tuple") and must not be `NULL`, and keyword arguments must be a [`dict`](../library/stdtypes.html#dict "dict") or `NULL`, whereas the removed functions checked argument types and accepted `NULL` positional and keyword arguments. To replace `PyEval_CallObjectWithKeywords(func, NULL, kwargs)` with [`PyObject_Call()`](../c-api/call.html#c.PyObject_Call "PyObject_Call"), pass an empty tuple as positional arguments using [`PyTuple_New(0)`](../c-api/tuple.html#c.PyTuple_New "PyTuple_New").
       
   *   `PyEval_CallFunction()`: Use [`PyObject_CallFunction()`](../c-api/call.html#c.PyObject_CallFunction "PyObject_CallFunction") instead.
       
   *   `PyEval_CallMethod()`: Use [`PyObject_CallMethod()`](../c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod") instead.
       
   *   `PyCFunction_Call()`: Use [`PyObject_Call()`](../c-api/call.html#c.PyObject_Call "PyObject_Call") instead.
       
   
   (Contributed by Victor Stinner in [gh-105107](https://github.com/python/cpython/issues/105107).)
   
*   Remove the following old functions to configure the Python initialization, deprecated in Python 3.11:
   
   *   `PySys_AddWarnOptionUnicode()`: Use [`PyConfig.warnoptions`](../c-api/init_config.html#c.PyConfig.warnoptions "PyConfig.warnoptions") instead.
       
   *   `PySys_AddWarnOption()`: Use [`PyConfig.warnoptions`](../c-api/init_config.html#c.PyConfig.warnoptions "PyConfig.warnoptions") instead.
       
   *   `PySys_AddXOption()`: Use [`PyConfig.xoptions`](../c-api/init_config.html#c.PyConfig.xoptions "PyConfig.xoptions") instead.
       
   *   `PySys_HasWarnOptions()`: Use [`PyConfig.xoptions`](../c-api/init_config.html#c.PyConfig.xoptions "PyConfig.xoptions") instead.
       
   *   `PySys_SetPath()`: Set [`PyConfig.module_search_paths`](../c-api/init_config.html#c.PyConfig.module_search_paths "PyConfig.module_search_paths") instead.
       
   *   `Py_SetPath()`: Set [`PyConfig.module_search_paths`](../c-api/init_config.html#c.PyConfig.module_search_paths "PyConfig.module_search_paths") instead.
       
   *   `Py_SetStandardStreamEncoding()`: Set [`PyConfig.stdio_encoding`](../c-api/init_config.html#c.PyConfig.stdio_encoding "PyConfig.stdio_encoding") instead, and set also maybe [`PyConfig.legacy_windows_stdio`](../c-api/init_config.html#c.PyConfig.legacy_windows_stdio "PyConfig.legacy_windows_stdio") (on Windows).
       
   *   `_Py_SetProgramFullPath()`: Set [`PyConfig.executable`](../c-api/init_config.html#c.PyConfig.executable "PyConfig.executable") instead.
       
   
   Use the new [`PyConfig`](../c-api/init_config.html#c.PyConfig "PyConfig") API of the [Python Initialization Configuration](../c-api/init_config.html#init-config) instead ([**PEP 587**](https://peps.python.org/pep-0587/)), added to Python 3.8. (Contributed by Victor Stinner in [gh-105145](https://github.com/python/cpython/issues/105145).)
   
*   Remove `PyEval_AcquireLock()` and `PyEval_ReleaseLock()` functions, deprecated in Python 3.2. They didn't update the current thread state. They can be replaced with:
   
   *   [`PyEval_SaveThread()`](../c-api/init.html#c.PyEval_SaveThread "PyEval_SaveThread") and [`PyEval_RestoreThread()`](../c-api/init.html#c.PyEval_RestoreThread "PyEval_RestoreThread");
       
   *   low-level [`PyEval_AcquireThread()`](../c-api/init.html#c.PyEval_AcquireThread "PyEval_AcquireThread") and [`PyEval_RestoreThread()`](../c-api/init.html#c.PyEval_RestoreThread "PyEval_RestoreThread");
       
   *   or [`PyGILState_Ensure()`](../c-api/init.html#c.PyGILState_Ensure "PyGILState_Ensure") and [`PyGILState_Release()`](../c-api/init.html#c.PyGILState_Release "PyGILState_Release").
       
   
   (Contributed by Victor Stinner in [gh-105182](https://github.com/python/cpython/issues/105182).)
   
*   删除了在 Python 3.9 弃用的:c:func:!PyEval\_ThreadsInitialized 函数。自Python 3.7 起，`Py_Initialize()` 总是创建全局解释器锁 ：调用:c:func:!PyEval\_InitThreads 不做任何事情，而:c:func:!PyEval\_ThreadsInitialized 总返回非零值。(由 Victor Stinner 在:gh:105182 中贡献。）
   
*   Remove the `_PyInterpreterState_Get()` alias to [`PyInterpreterState_Get()`](../c-api/init.html#c.PyInterpreterState_Get "PyInterpreterState_Get") which was kept for backward compatibility with Python 3.8. The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/) can be used to get [`PyInterpreterState_Get()`](../c-api/init.html#c.PyInterpreterState_Get "PyInterpreterState_Get") on Python 3.8 and older. (Contributed by Victor Stinner in [gh-106320](https://github.com/python/cpython/issues/106320).)
   
*   Remove the private `_PyObject_FastCall()` function: use `PyObject_Vectorcall()` which is available since Python 3.8 ([**PEP 590**](https://peps.python.org/pep-0590/)). (Contributed by Victor Stinner in [gh-106023](https://github.com/python/cpython/issues/106023).)
   
*   Remove the `cpython/pytime.h` header file, which only contained private functions. (Contributed by Victor Stinner in [gh-106316](https://github.com/python/cpython/issues/106316).)
   
*   Remove the undocumented `PY_TIMEOUT_MAX` constant from the limited C API. (Contributed by Victor Stinner in [gh-110014](https://github.com/python/cpython/issues/110014).)
   
*   Remove the old trashcan macros `Py_TRASHCAN_SAFE_BEGIN` and `Py_TRASHCAN_SAFE_END`. Replace both with the new macros `Py_TRASHCAN_BEGIN` and `Py_TRASHCAN_END`. (Contributed by Irit Katriel in [gh-105111](https://github.com/python/cpython/issues/105111).)
   

### 已弃用的 C API[¶](#deprecated-c-apis "Link to this heading")

*   已弃用旧的 Python 初始化函数：
   
   *   [`PySys_ResetWarnOptions()`](../c-api/sys.html#c.PySys_ResetWarnOptions "PySys_ResetWarnOptions"): 改为清除 [`sys.warnoptions`](../library/sys.html#sys.warnoptions "sys.warnoptions") 和 `warnings.filters`。
       
   *   [`Py_GetExecPrefix()`](../c-api/init.html#c.Py_GetExecPrefix "Py_GetExecPrefix"): 改为获取 [`sys.exec_prefix`](../library/sys.html#sys.exec_prefix "sys.exec_prefix")。
       
   *   [`Py_GetPath()`](../c-api/init.html#c.Py_GetPath "Py_GetPath"): 改为获取 [`sys.path`](../library/sys.html#sys.path "sys.path")。
       
   *   [`Py_GetPrefix()`](../c-api/init.html#c.Py_GetPrefix "Py_GetPrefix"): 改为获取 [`sys.prefix`](../library/sys.html#sys.prefix "sys.prefix")。
       
   *   [`Py_GetProgramFullPath()`](../c-api/init.html#c.Py_GetProgramFullPath "Py_GetProgramFullPath"): 改为获取 [`sys.executable`](../library/sys.html#sys.executable "sys.executable")。
       
   *   [`Py_GetProgramName()`](../c-api/init.html#c.Py_GetProgramName "Py_GetProgramName"): 改为获取 [`sys.executable`](../library/sys.html#sys.executable "sys.executable")。
       
   *   [`Py_GetPythonHome()`](../c-api/init.html#c.Py_GetPythonHome "Py_GetPythonHome"): 改为获取 [`PyConfig.home`](../c-api/init_config.html#c.PyConfig.home "PyConfig.home") 或 [`PYTHONHOME`](../using/cmdline.html#envvar-PYTHONHOME) 环境变量。
       
   
   （由 Victor Stinner 在 [gh-105145](https://github.com/python/cpython/issues/105145) 中贡献。）
   
*   [Soft deprecate](../glossary.html#term-soft-deprecated) the [`PyEval_GetBuiltins()`](../c-api/reflection.html#c.PyEval_GetBuiltins "PyEval_GetBuiltins"), [`PyEval_GetGlobals()`](../c-api/reflection.html#c.PyEval_GetGlobals "PyEval_GetGlobals"), and [`PyEval_GetLocals()`](../c-api/reflection.html#c.PyEval_GetLocals "PyEval_GetLocals") functions, which return a [borrowed reference](../glossary.html#term-borrowed-reference). (Soft deprecated as part of [**PEP 667**](https://peps.python.org/pep-0667/).)
   
*   Deprecate the [`PyImport_ImportModuleNoBlock()`](../c-api/import.html#c.PyImport_ImportModuleNoBlock "PyImport_ImportModuleNoBlock") function, which is just an alias to [`PyImport_ImportModule()`](../c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule") since Python 3.3. (Contributed by Victor Stinner in [gh-105396](https://github.com/python/cpython/issues/105396).)
   
*   [Soft deprecate](../glossary.html#term-soft-deprecated) the [`PyModule_AddObject()`](../c-api/module.html#c.PyModule_AddObject "PyModule_AddObject") function. It should be replaced with [`PyModule_Add()`](../c-api/module.html#c.PyModule_Add "PyModule_Add") or [`PyModule_AddObjectRef()`](../c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef"). (Contributed by Serhiy Storchaka in [gh-86493](https://github.com/python/cpython/issues/86493).)
   
*   Deprecate the old `Py_UNICODE` and `PY_UNICODE_TYPE` types and the `Py_UNICODE_WIDE` define. Use the `wchar_t` type directly instead. Since Python 3.3, `Py_UNICODE` and `PY_UNICODE_TYPE` are just aliases to `wchar_t`. (Contributed by Victor Stinner in [gh-105156](https://github.com/python/cpython/issues/105156).)
   
*   Deprecate the [`PyWeakref_GetObject()`](../c-api/weakref.html#c.PyWeakref_GetObject "PyWeakref_GetObject") and [`PyWeakref_GET_OBJECT()`](../c-api/weakref.html#c.PyWeakref_GET_OBJECT "PyWeakref_GET_OBJECT") functions, which return a [borrowed reference](../glossary.html#term-borrowed-reference). Replace them with the new [`PyWeakref_GetRef()`](../c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef") function, which returns a [strong reference](../glossary.html#term-strong-reference). The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/) can be used to get [`PyWeakref_GetRef()`](../c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef") on Python 3.12 and older. (Contributed by Victor Stinner in [gh-105927](https://github.com/python/cpython/issues/105927).)
   

#### Pending removal in Python 3.14[¶](#id8 "Link to this heading")

*   [`PyDictObject`](../c-api/dict.html#c.PyDictObject "PyDictObject") 中的 `ma_version_tag` 字段用于扩展模块 ( [**PEP 699**](https://peps.python.org/pep-0699/) ; [gh-101193](https://github.com/python/cpython/issues/101193) )。
   
*   创建 [`immutable types`](../c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE") 的可变基础 ( [gh-95388](https://github.com/python/cpython/issues/95388) )。
   
*   用于配置 Python 的初始化的函数，在 Python 3.11 中已弃用：
   
   *   `PySys_SetArgvEx()`: 改为设置 [`PyConfig.argv`](../c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")。
       
   *   `PySys_SetArgv()`: 改为设置 [`PyConfig.argv`](../c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")。
       
   *   `Py_SetProgramName()`: 改为设置 [`PyConfig.program_name`](../c-api/init_config.html#c.PyConfig.program_name "PyConfig.program_name")。
       
   *   `Py_SetPythonHome()`: 改为设置 [`PyConfig.home`](../c-api/init_config.html#c.PyConfig.home "PyConfig.home")。
       
   
   [`Py_InitializeFromConfig()`](../c-api/init.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig") API 应与 [`PyConfig`](../c-api/init_config.html#c.PyConfig "PyConfig") 一起使用。
   
*   全局配置变量：
   
   *   [`Py_DebugFlag`](../c-api/init.html#c.Py_DebugFlag "Py_DebugFlag"): 改用 [`PyConfig.parser_debug`](../c-api/init_config.html#c.PyConfig.parser_debug "PyConfig.parser_debug")。
       
   *   [`Py_VerboseFlag`](../c-api/init.html#c.Py_VerboseFlag "Py_VerboseFlag"): 改用 [`PyConfig.verbose`](../c-api/init_config.html#c.PyConfig.verbose "PyConfig.verbose")。
       
   *   [`Py_QuietFlag`](../c-api/init.html#c.Py_QuietFlag "Py_QuietFlag"): 改用 [`PyConfig.quiet`](../c-api/init_config.html#c.PyConfig.quiet "PyConfig.quiet")。
       
   *   [`Py_InteractiveFlag`](../c-api/init.html#c.Py_InteractiveFlag "Py_InteractiveFlag"): 改用 [`PyConfig.interactive`](../c-api/init_config.html#c.PyConfig.interactive "PyConfig.interactive")。
       
   *   [`Py_InspectFlag`](../c-api/init.html#c.Py_InspectFlag "Py_InspectFlag"): 改用 [`PyConfig.inspect`](../c-api/init_config.html#c.PyConfig.inspect "PyConfig.inspect")。
       
   *   [`Py_OptimizeFlag`](../c-api/init.html#c.Py_OptimizeFlag "Py_OptimizeFlag"): 改用 [`PyConfig.optimization_level`](../c-api/init_config.html#c.PyConfig.optimization_level "PyConfig.optimization_level")。
       
   *   [`Py_NoSiteFlag`](../c-api/init.html#c.Py_NoSiteFlag "Py_NoSiteFlag"): 改用 [`PyConfig.site_import`](../c-api/init_config.html#c.PyConfig.site_import "PyConfig.site_import")。
       
   *   [`Py_BytesWarningFlag`](../c-api/init.html#c.Py_BytesWarningFlag "Py_BytesWarningFlag"): 改用 [`PyConfig.bytes_warning`](../c-api/init_config.html#c.PyConfig.bytes_warning "PyConfig.bytes_warning")。
       
   *   [`Py_FrozenFlag`](../c-api/init.html#c.Py_FrozenFlag "Py_FrozenFlag"): 改用 [`PyConfig.pathconfig_warnings`](../c-api/init_config.html#c.PyConfig.pathconfig_warnings "PyConfig.pathconfig_warnings")。
       
   *   [`Py_IgnoreEnvironmentFlag`](../c-api/init.html#c.Py_IgnoreEnvironmentFlag "Py_IgnoreEnvironmentFlag"): 改用 [`PyConfig.use_environment`](../c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment")。
       
   *   [`Py_DontWriteBytecodeFlag`](../c-api/init.html#c.Py_DontWriteBytecodeFlag "Py_DontWriteBytecodeFlag"): 改用 [`PyConfig.write_bytecode`](../c-api/init_config.html#c.PyConfig.write_bytecode "PyConfig.write_bytecode")。
       
   *   [`Py_NoUserSiteDirectory`](../c-api/init.html#c.Py_NoUserSiteDirectory "Py_NoUserSiteDirectory"): 改用 [`PyConfig.user_site_directory`](../c-api/init_config.html#c.PyConfig.user_site_directory "PyConfig.user_site_directory")。
       
   *   [`Py_UnbufferedStdioFlag`](../c-api/init.html#c.Py_UnbufferedStdioFlag "Py_UnbufferedStdioFlag"): 改用 [`PyConfig.buffered_stdio`](../c-api/init_config.html#c.PyConfig.buffered_stdio "PyConfig.buffered_stdio")。
       
   *   [`Py_HashRandomizationFlag`](../c-api/init.html#c.Py_HashRandomizationFlag "Py_HashRandomizationFlag"): 改用 [`PyConfig.use_hash_seed`](../c-api/init_config.html#c.PyConfig.use_hash_seed "PyConfig.use_hash_seed") 和 [`PyConfig.hash_seed`](../c-api/init_config.html#c.PyConfig.hash_seed "PyConfig.hash_seed")。
       
   *   [`Py_IsolatedFlag`](../c-api/init.html#c.Py_IsolatedFlag "Py_IsolatedFlag"): 改用 [`PyConfig.isolated`](../c-api/init_config.html#c.PyConfig.isolated "PyConfig.isolated")。
       
   *   [`Py_LegacyWindowsFSEncodingFlag`](../c-api/init.html#c.Py_LegacyWindowsFSEncodingFlag "Py_LegacyWindowsFSEncodingFlag"): 改用 [`PyPreConfig.legacy_windows_fs_encoding`](../c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "PyPreConfig.legacy_windows_fs_encoding")。
       
   *   [`Py_LegacyWindowsStdioFlag`](../c-api/init.html#c.Py_LegacyWindowsStdioFlag "Py_LegacyWindowsStdioFlag"): 改用 [`PyConfig.legacy_windows_stdio`](../c-api/init_config.html#c.PyConfig.legacy_windows_stdio "PyConfig.legacy_windows_stdio")。
       
   *   `Py_FileSystemDefaultEncoding`: 改用 [`PyConfig.filesystem_encoding`](../c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")。
       
   *   `Py_HasFileSystemDefaultEncoding`: 改用 [`PyConfig.filesystem_encoding`](../c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")。
       
   *   `Py_FileSystemDefaultEncodeErrors`: 改用 [`PyConfig.filesystem_errors`](../c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")。
       
   *   `Py_UTF8Mode`: 改用 [`PyPreConfig.utf8_mode`](../c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode")。 (参见 [`Py_PreInitialize()`](../c-api/init_config.html#c.Py_PreInitialize "Py_PreInitialize"))
       
   
   [`Py_InitializeFromConfig()`](../c-api/init.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig") API 应与 [`PyConfig`](../c-api/init_config.html#c.PyConfig "PyConfig") 一起使用。
   

#### Pending removal in Python 3.15[¶](#id9 "Link to this heading")

*   捆绑的 `libmpdecimal` 副本。
   
*   The [`PyImport_ImportModuleNoBlock()`](../c-api/import.html#c.PyImport_ImportModuleNoBlock "PyImport_ImportModuleNoBlock"): 改用 [`PyImport_ImportModule()`](../c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")。
   
*   [`PyWeakref_GetObject()`](../c-api/weakref.html#c.PyWeakref_GetObject "PyWeakref_GetObject") 和 [`PyWeakref_GET_OBJECT()`](../c-api/weakref.html#c.PyWeakref_GET_OBJECT "PyWeakref_GET_OBJECT"): 改用 [`PyWeakref_GetRef()`](../c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef")。
   
*   [`Py_UNICODE`](../c-api/unicode.html#c.Py_UNICODE "Py_UNICODE") 类型和 `Py_UNICODE_WIDE` 宏：改用 `wchar_t`。
   
*   Python 初始化函数
   
   *   [`PySys_ResetWarnOptions()`](../c-api/sys.html#c.PySys_ResetWarnOptions "PySys_ResetWarnOptions"): 改为清除 [`sys.warnoptions`](../library/sys.html#sys.warnoptions "sys.warnoptions") 和 `warnings.filters`。
       
   *   [`Py_GetExecPrefix()`](../c-api/init.html#c.Py_GetExecPrefix "Py_GetExecPrefix"): Get [`sys.base_exec_prefix`](../library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix") and [`sys.exec_prefix`](../library/sys.html#sys.exec_prefix "sys.exec_prefix") instead.
       
   *   [`Py_GetPath()`](../c-api/init.html#c.Py_GetPath "Py_GetPath"): 改为获取 [`sys.path`](../library/sys.html#sys.path "sys.path")。
       
   *   [`Py_GetPrefix()`](../c-api/init.html#c.Py_GetPrefix "Py_GetPrefix"): Get [`sys.base_prefix`](../library/sys.html#sys.base_prefix "sys.base_prefix") and [`sys.prefix`](../library/sys.html#sys.prefix "sys.prefix") instead.
       
   *   [`Py_GetProgramFullPath()`](../c-api/init.html#c.Py_GetProgramFullPath "Py_GetProgramFullPath"): 改为获取 [`sys.executable`](../library/sys.html#sys.executable "sys.executable")。
       
   *   [`Py_GetProgramName()`](../c-api/init.html#c.Py_GetProgramName "Py_GetProgramName"): 改为获取 [`sys.executable`](../library/sys.html#sys.executable "sys.executable")。
       
   *   [`Py_GetPythonHome()`](../c-api/init.html#c.Py_GetPythonHome "Py_GetPythonHome"): 改为获取 [`PyConfig.home`](../c-api/init_config.html#c.PyConfig.home "PyConfig.home") 或 [`PYTHONHOME`](../using/cmdline.html#envvar-PYTHONHOME) 环境变量。
       

#### Pending removal in future versions[¶](#id10 "Link to this heading")

以下 API 已被弃用，将被移除，但目前尚未确定移除日期。

*   [`Py_TPFLAGS_HAVE_FINALIZE`](../c-api/typeobj.html#c.Py_TPFLAGS_HAVE_FINALIZE "Py_TPFLAGS_HAVE_FINALIZE"): 自 Python 3.8 起不再需要。
   
*   [`PyErr_Fetch()`](../c-api/exceptions.html#c.PyErr_Fetch "PyErr_Fetch"): 改用 [`PyErr_GetRaisedException()`](../c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")。
   
*   [`PyErr_NormalizeException()`](../c-api/exceptions.html#c.PyErr_NormalizeException "PyErr_NormalizeException"): 改用 [`PyErr_GetRaisedException()`](../c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")。
   
*   [`PyErr_Restore()`](../c-api/exceptions.html#c.PyErr_Restore "PyErr_Restore"): 改用 [`PyErr_SetRaisedException()`](../c-api/exceptions.html#c.PyErr_SetRaisedException "PyErr_SetRaisedException")。
   
*   [`PyModule_GetFilename()`](../c-api/module.html#c.PyModule_GetFilename "PyModule_GetFilename"): 改用 [`PyModule_GetFilenameObject()`](../c-api/module.html#c.PyModule_GetFilenameObject "PyModule_GetFilenameObject")。
   
*   [`PyOS_AfterFork()`](../c-api/sys.html#c.PyOS_AfterFork "PyOS_AfterFork"): 改用 [`PyOS_AfterFork_Child()`](../c-api/sys.html#c.PyOS_AfterFork_Child "PyOS_AfterFork_Child")。
   
*   [`PySlice_GetIndicesEx()`](../c-api/slice.html#c.PySlice_GetIndicesEx "PySlice_GetIndicesEx"): 改用 [`PySlice_Unpack()`](../c-api/slice.html#c.PySlice_Unpack "PySlice_Unpack") and [`PySlice_AdjustIndices()`](../c-api/slice.html#c.PySlice_AdjustIndices "PySlice_AdjustIndices")。
   
*   `PyUnicode_AsDecodedObject()`: 改用 [`PyCodec_Decode()`](../c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")。
   
*   `PyUnicode_AsDecodedUnicode()`: 改用 [`PyCodec_Decode()`](../c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")。
   
*   `PyUnicode_AsEncodedObject()`: 改用 [`PyCodec_Encode()`](../c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")。
   
*   `PyUnicode_AsEncodedUnicode()`: 改用 [`PyCodec_Encode()`](../c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")。
   
*   [`PyUnicode_READY()`](../c-api/unicode.html#c.PyUnicode_READY "PyUnicode_READY"): 自 Python 3.12 起不再需要
   
*   `PyErr_Display()`: 改用 [`PyErr_DisplayException()`](../c-api/exceptions.html#c.PyErr_DisplayException "PyErr_DisplayException")。
   
*   `_PyErr_ChainExceptions()`: 改用 `_PyErr_ChainExceptions1()`。
   
*   `PyBytesObject.ob_shash` 成员：改为调用 [`PyObject_Hash()`](../c-api/object.html#c.PyObject_Hash "PyObject_Hash")。
   
*   `PyDictObject.ma_version_tag` 成员。
   
*   线程本地存储 (TLS) API：
   
   *   [`PyThread_create_key()`](../c-api/init.html#c.PyThread_create_key "PyThread_create_key"): 改用 [`PyThread_tss_alloc()`](../c-api/init.html#c.PyThread_tss_alloc "PyThread_tss_alloc")。
       
   *   [`PyThread_delete_key()`](../c-api/init.html#c.PyThread_delete_key "PyThread_delete_key"): 改用 [`PyThread_tss_free()`](../c-api/init.html#c.PyThread_tss_free "PyThread_tss_free")。
       
   *   [`PyThread_set_key_value()`](../c-api/init.html#c.PyThread_set_key_value "PyThread_set_key_value"): 改用 [`PyThread_tss_set()`](../c-api/init.html#c.PyThread_tss_set "PyThread_tss_set")。
       
   *   [`PyThread_get_key_value()`](../c-api/init.html#c.PyThread_get_key_value "PyThread_get_key_value"): 改用 [`PyThread_tss_get()`](../c-api/init.html#c.PyThread_tss_get "PyThread_tss_get")。
       
   *   [`PyThread_delete_key_value()`](../c-api/init.html#c.PyThread_delete_key_value "PyThread_delete_key_value"): 改用 [`PyThread_tss_delete()`](../c-api/init.html#c.PyThread_tss_delete "PyThread_tss_delete")。
       
   *   [`PyThread_ReInitTLS()`](../c-api/init.html#c.PyThread_ReInitTLS "PyThread_ReInitTLS"): 自 Python 3.7 起不再需要。
       

构建变化[¶](#build-changes "Link to this heading")
----------------------------------------------

*   `arm64-apple-ios` and `arm64-apple-ios-simulator` are both now [**PEP 11**](https://peps.python.org/pep-0011/) tier 3 platforms. ([PEP 730](#whatsnew313-platform-support) written and implementation contributed by Russell Keith-Magee in [gh-114099](https://github.com/python/cpython/issues/114099).)
   
*   `aarch64-linux-android` and `x86_64-linux-android` are both now [**PEP 11**](https://peps.python.org/pep-0011/) tier 3 platforms. ([PEP 738](#whatsnew313-platform-support) written and implementation contributed by Malcolm Smith in [gh-116622](https://github.com/python/cpython/issues/116622).)
   
*   现在 `wasm32-wasi` 是 [**PEP 11**](https://peps.python.org/pep-0011/) 第 2 层级的平台。 （由 Brett Cannon 在 [gh-115192](https://github.com/python/cpython/issues/115192) 中贡献。）
   
*   `wasm32-emscripten` 不再是 [**PEP 11**](https://peps.python.org/pep-0011/) 的受支持平台。 （由 Brett Cannon 在 [gh-115192](https://github.com/python/cpython/issues/115192) 中贡献。）
   
*   现在构建 CPython 需要带有 C11 atomic 库支持的编译器、GCC 内置 atomic 函数或 MSVC 互锁内生函数。
   
*   Autoconf 2.71 and aclocal 1.16.5 are now required to regenerate the `configure` script. (Contributed by Christian Heimes in [gh-89886](https://github.com/python/cpython/issues/89886) and by Victor Stinner in [gh-112090](https://github.com/python/cpython/issues/112090).)
   
*   需要 SQLite 3.15.2 或更新的版本才能构建 [`sqlite3`](../library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.") 扩展模块。 （由 Erlend Aasland 在 [gh-105875](https://github.com/python/cpython/issues/105875) 中贡献。）
   
*   CPython now bundles the [mimalloc library](https://github.com/microsoft/mimalloc/) by default. It is licensed under the MIT license; see [mimalloc license](../license.html#mimalloc-license). The bundled mimalloc has custom changes, see [gh-113141](https://github.com/python/cpython/issues/113141) for details. (Contributed by Dino Viehland in [gh-109914](https://github.com/python/cpython/issues/109914).)
   
*   现在 `configure` 选项 [`--with-system-libmpdec`](../using/configure.html#cmdoption-with-system-libmpdec) 默认为 `yes`。 捆绑的 `libmpdecimal` 副本将在 Python 3.15 中被移除。
   
*   使用 `configure` [`--with-trace-refs`](../using/configure.html#cmdoption-with-trace-refs) (跟踪引用) 构建的 Python 现在与 Python 发布构建版和 [调试构建版](../using/configure.html#debug-build) 是 ABI 兼容的。 （由 Victor Stinner 在 [gh-108634](https://github.com/python/cpython/issues/108634) 中贡献。）
   
*   On POSIX systems, the pkg-config (`.pc`) filenames now include the ABI flags. For example, the free-threaded build generates `python-3.13t.pc` and the debug build generates `python-3.13d.pc`.
   
*   现在 `errno`, `fcntl`, `grp`, `md5`, `pwd`, `resource`, `termios`, `winsound`, `_ctypes_test`, `_multiprocessing.posixshmem`, `_scproxy`, `_stat`, `_statistics`, `_testconsole`, `_testimportmultiple` 和 `_uuid` C 扩展是使用 [受限 C API](../c-api/stable.html#limited-c-api) 构建的。 （由 Victor Stinner 在 [gh-85283](https://github.com/python/cpython/issues/85283) 中贡献。）
   

Porting to Python 3.13[¶](#porting-to-python-3-13 "Link to this heading")
-------------------------------------------------------------------------

本节列出了先前描述的更改以及可能需要更改代码的其他错误修正.

### Python API 的变化[¶](#changes-in-the-python-api "Link to this heading")

*   [PEP 667](#whatsnew313-locals-semantics) introduces several changes to the semantics of [`locals()`](../library/functions.html#locals "locals") and [`f_locals`](../reference/datamodel.html#frame.f_locals "frame.f_locals"):
   
   *   Calling [`locals()`](../library/functions.html#locals "locals") in an [optimized scope](../glossary.html#term-optimized-scope) now produces an independent snapshot on each call, and hence no longer implicitly updates previously returned references. Obtaining the legacy CPython behavior now requires explicit calls to update the initially returned dictionary with the results of subsequent calls to `locals()`. Code execution functions that implicitly target `locals()` (such as `exec` and `eval`) must be passed an explicit namespace to access their results in an optimized scope. (Changed as part of [**PEP 667**](https://peps.python.org/pep-0667/).)
       
   *   Calling [`locals()`](../library/functions.html#locals "locals") from a comprehension at module or class scope (including via `exec` or `eval`) once more behaves as if the comprehension were running as an independent nested function (i.e. the local variables from the containing scope are not included). In Python 3.12, this had changed to include the local variables from the containing scope when implementing [**PEP 709**](https://peps.python.org/pep-0709/). (Changed as part of [**PEP 667**](https://peps.python.org/pep-0667/).)
       
   *   Accessing [`FrameType.f_locals`](../reference/datamodel.html#frame.f_locals "frame.f_locals") in an [optimized scope](../glossary.html#term-optimized-scope) now returns a write-through proxy rather than a snapshot that gets updated at ill-specified times. If a snapshot is desired, it must be created explicitly with `dict` or the proxy's `.copy()` method. (Changed as part of [**PEP 667**](https://peps.python.org/pep-0667/).)
       
*   [`functools.partial`](../library/functools.html#functools.partial "functools.partial") now emits a [`FutureWarning`](../library/exceptions.html#FutureWarning "FutureWarning") when used as a method. The behavior will change in future Python versions. Wrap it in [`staticmethod()`](../library/functions.html#staticmethod "staticmethod") if you want to preserve the old behavior. (Contributed by Serhiy Storchaka in [gh-121027](https://github.com/python/cpython/issues/121027).)
   
*   An [`OSError`](../library/exceptions.html#OSError "OSError") is now raised by [`getpass.getuser()`](../library/getpass.html#getpass.getuser "getpass.getuser") for any failure to retrieve a username, instead of [`ImportError`](../library/exceptions.html#ImportError "ImportError") on non-Unix platforms or [`KeyError`](../library/exceptions.html#KeyError "KeyError") on Unix platforms where the password database is empty.
   
*   The value of the `mode` attribute of [`gzip.GzipFile`](../library/gzip.html#gzip.GzipFile "gzip.GzipFile") is now a string (`'rb'` or `'wb'`) instead of an integer (`1` or `2`). The value of the `mode` attribute of the readable file-like object returned by [`zipfile.ZipFile.open()`](../library/zipfile.html#zipfile.ZipFile.open "zipfile.ZipFile.open") is now `'rb'` instead of `'r'`. (Contributed by Serhiy Storchaka in [gh-115961](https://github.com/python/cpython/issues/115961).)
   
*   [`mailbox.Maildir`](../library/mailbox.html#mailbox.Maildir "mailbox.Maildir") now ignores files with a leading dot (`.`). (Contributed by Zackery Spytz in [gh-65559](https://github.com/python/cpython/issues/65559).)
   
*   [`pathlib.Path.glob()`](../library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob") and [`rglob()`](../library/pathlib.html#pathlib.Path.rglob "pathlib.Path.rglob") now return both files and directories if a pattern that ends with "`**`" is given, rather than directories only. Add a trailing slash to keep the previous behavior and only match directories.
   
*   The [`threading`](../library/threading.html#module-threading "threading: Thread-based parallelism.") module now expects the `_thread` module to have an `_is_main_interpreter()` function. This function takes no arguments and returns `True` if the current interpreter is the main interpreter.
   
   Any library or application that provides a custom `_thread` module must provide `_is_main_interpreter()`, just like the module's other "private" attributes. ([gh-112826](https://github.com/python/cpython/issues/112826).)
   

### C API 的变化[¶](#changes-in-the-c-api "Link to this heading")

*   `Python.h` no longer includes the `<ieeefp.h>` standard header. It was included for the `finite()` function which is now provided by the `<math.h>` header. It should now be included explicitly if needed. Remove also the `HAVE_IEEEFP_H` macro. (Contributed by Victor Stinner in [gh-108765](https://github.com/python/cpython/issues/108765).)
   
*   `Python.h` no longer includes these standard header files: `<time.h>`, `<sys/select.h>` and `<sys/time.h>`. If needed, they should now be included explicitly. For example, `<time.h>` provides the `clock()` and `gmtime()` functions, `<sys/select.h>` provides the `select()` function, and `<sys/time.h>` provides the `futimes()`, `gettimeofday()` and `setitimer()` functions. (Contributed by Victor Stinner in [gh-108765](https://github.com/python/cpython/issues/108765).)
   
*   On Windows, `Python.h` no longer includes the `<stddef.h>` standard header file. If needed, it should now be included explicitly. For example, it provides `offsetof()` function, and `size_t` and `ptrdiff_t` types. Including `<stddef.h>` explicitly was already needed by all other platforms, the `HAVE_STDDEF_H` macro is only defined on Windows. (Contributed by Victor Stinner in [gh-108765](https://github.com/python/cpython/issues/108765).)
   
*   If the [`Py_LIMITED_API`](../c-api/stable.html#c.Py_LIMITED_API "Py_LIMITED_API") macro is defined, `Py_BUILD_CORE`, `Py_BUILD_CORE_BUILTIN` and `Py_BUILD_CORE_MODULE` macros are now undefined by `<Python.h>`. (Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283).)
   
*   The old trashcan macros `Py_TRASHCAN_SAFE_BEGIN` and `Py_TRASHCAN_SAFE_END` were removed. They should be replaced by the new macros `Py_TRASHCAN_BEGIN` and `Py_TRASHCAN_END`.
   
   A `tp_dealloc` function that has the old macros, such as:
   
   static void
   mytype\_dealloc(mytype \*p)
   {
       PyObject\_GC\_UnTrack(p);
       Py\_TRASHCAN\_SAFE\_BEGIN(p);
       ...
       Py\_TRASHCAN\_SAFE\_END
   }
   
   应当按照以下方式迁移到新版宏:
   
   static void
   mytype\_dealloc(mytype \*p)
   {
       PyObject\_GC\_UnTrack(p);
       Py\_TRASHCAN\_BEGIN(p, mytype\_dealloc)
       ...
       Py\_TRASHCAN\_END
   }
   
   Note that `Py_TRASHCAN_BEGIN` has a second argument which should be the deallocation function it is in. The new macros were added in Python 3.8 and the old macros were deprecated in Python 3.11. (Contributed by Irit Katriel in [gh-105111](https://github.com/python/cpython/issues/105111).)
   

*   [PEP 667](#whatsnew313-locals-semantics) introduces several changes to frame-related functions:
   
   *   The effects of mutating the dictionary returned from [`PyEval_GetLocals()`](../c-api/reflection.html#c.PyEval_GetLocals "PyEval_GetLocals") in an [optimized scope](../glossary.html#term-optimized-scope) have changed. New dict entries added this way will now _only_ be visible to subsequent [`PyEval_GetLocals()`](../c-api/reflection.html#c.PyEval_GetLocals "PyEval_GetLocals") calls in that frame, as [`PyFrame_GetLocals()`](../c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals"), [`locals()`](../library/functions.html#locals "locals"), and [`FrameType.f_locals`](../reference/datamodel.html#frame.f_locals "frame.f_locals") no longer access the same underlying cached dictionary. Changes made to entries for actual variable names and names added via the write-through proxy interfaces will be overwritten on subsequent calls to [`PyEval_GetLocals()`](../c-api/reflection.html#c.PyEval_GetLocals "PyEval_GetLocals") in that frame. The recommended code update depends on how the function was being used, so refer to the deprecation notice on the function for details.
       
   *   Calling [`PyFrame_GetLocals()`](../c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals") in an [optimized scope](../glossary.html#term-optimized-scope) now returns a write-through proxy rather than a snapshot that gets updated at ill-specified times. If a snapshot is desired, it must be created explicitly (e.g. with [`PyDict_Copy()`](../c-api/dict.html#c.PyDict_Copy "PyDict_Copy")), or by calling the new [`PyEval_GetFrameLocals()`](../c-api/reflection.html#c.PyEval_GetFrameLocals "PyEval_GetFrameLocals") API.
       
   *   `PyFrame_FastToLocals()` and `PyFrame_FastToLocalsWithError()` no longer have any effect. Calling these functions has been redundant since Python 3.11, when [`PyFrame_GetLocals()`](../c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals") was first introduced.
       
   *   `PyFrame_LocalsToFast()` no longer has any effect. Calling this function is redundant now that [`PyFrame_GetLocals()`](../c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals") returns a write-through proxy for [optimized scopes](../glossary.html#term-optimized-scope).
       

回归测试的变化[¶](#regression-test-changes "Link to this heading")
-----------------------------------------------------------

*   现在使用 `configure` [`--with-pydebug`](../using/configure.html#cmdoption-with-pydebug) 编译的 Python 将支持 [`-X presite=package.module`](../using/cmdline.html#cmdoption-X) 命令行选项。 如果被使用，它指明一个模块应当在解释器生命周期开始时，即 `site.py` 被执行之前被导入。 （由 Łukasz Langa 在 [gh-110769](https://github.com/python/cpython/issues/110769) 中贡献。）
   

### [目录](../contents.html)

*   [Python 3.13 有什么新变化](#)
   *   [摘要 -- 发布重点](#summary-release-highlights)
   *   [新的特性](#new-features)
       *   [更好的交互式解释器](#a-better-interactive-interpreter)
       *   [改进的错误消息](#improved-error-messages)
       *   [自由线程的 CPython](#free-threaded-cpython)
       *   [实验性的即时 (JIT) 编译器](#an-experimental-just-in-time-jit-compiler)
       *   [针对 `locals()` 的已定义修改语义](#defined-mutation-semantics-for-locals)
       *   [对移动平台的支持](#support-for-mobile-platforms)
   *   [其他语言特性修改](#other-language-changes)
   *   [新增模块](#new-modules)
   *   [改进的模块](#improved-modules)
       *   [argparse](#argparse)
       *   [array](#array)
       *   [ast](#ast)
       *   [asyncio](#asyncio)
       *   [base64](#base64)
       *   [compileall](#compileall)
       *   [concurrent.futures](#concurrent-futures)
       *   [configparser](#configparser)
       *   [copy](#copy)
       *   [ctypes](#ctypes)
       *   [dbm](#dbm)
       *   [dis](#dis)
       *   [doctest](#doctest)
       *   [email](#email)
       *   [fractions](#fractions)
       *   [glob](#glob)
       *   [importlib](#importlib)
       *   [io](#io)
       *   [ipaddress](#ipaddress)
       *   [itertools](#itertools)
       *   [marshal](#marshal)
       *   [math](#math)
       *   [mimetypes](#mimetypes)
       *   [mmap](#mmap)
       *   [multiprocessing](#multiprocessing)
       *   [os](#os)
       *   [os.path](#os-path)
       *   [pathlib](#pathlib)
       *   [pdb](#pdb)
       *   [queue](#queue)
       *   [random](#random)
       *   [re](#re)
       *   [shutil](#shutil)
       *   [site](#site)
       *   [sqlite3](#sqlite3)
       *   [ssl](#ssl)
       *   [statistics](#statistics)
       *   [subprocess](#subprocess)
       *   [sys](#sys)
       *   [tempfile](#tempfile)
       *   [time](#time)
       *   [tkinter](#tkinter)
       *   [回溯](#traceback)
       *   [types](#types)
       *   [typing](#typing)
       *   [unicodedata](#unicodedata)
       *   [venv](#venv)
       *   [warnings](#warnings)
       *   [xml](#xml)
       *   [zipimport](#zipimport)
   *   [性能优化](#optimizations)
   *   [被移除的模块与 API](#removed-modules-and-apis)
       *   [PEP 594: 从标准库中移除“死电池”](#pep-594-remove-dead-batteries-from-the-standard-library)
       *   [2to3](#to3)
       *   [builtins](#builtins)
       *   [configparser](#id3)
       *   [importlib.metadata](#importlib-metadata)
       *   [locale](#locale)
       *   [opcode](#opcode)
       *   [pathlib](#id4)
       *   [re](#id5)
       *   [tkinter.tix](#tkinter-tix)
       *   [turtle](#turtle)
       *   [typing](#id6)
       *   [unittest](#unittest)
       *   [urllib](#urllib)
       *   [webbrowser](#webbrowser)
   *   [新的弃用](#new-deprecations)
       *   [Pending removal in Python 3.14](#pending-removal-in-python-3-14)
       *   [Pending removal in Python 3.15](#pending-removal-in-python-3-15)
       *   [Pending removal in Python 3.16](#pending-removal-in-python-3-16)
       *   [Pending removal in future versions](#pending-removal-in-future-versions)
   *   [CPython 字节码的变化](#cpython-bytecode-changes)
   *   [C API 的变化](#c-api-changes)
       *   [新的特性](#id7)
       *   [被改变的 C API](#changed-c-apis)
       *   [受限 C API 的改变](#limited-c-api-changes)
       *   [Removed C APIs](#removed-c-apis)
       *   [已弃用的 C API](#deprecated-c-apis)
           *   [Pending removal in Python 3.14](#id8)
           *   [Pending removal in Python 3.15](#id9)
           *   [Pending removal in future versions](#id10)
   *   [构建变化](#build-changes)
   *   [Porting to Python 3.13](#porting-to-python-3-13)
       *   [Python API 的变化](#changes-in-the-python-api)
       *   [C API 的变化](#changes-in-the-c-api)
   *   [回归测试的变化](#regression-test-changes)

#### 上一主题

[What's new in Python 3.14](3.14.html "上一章")

#### 下一主题

[Python 3.12 有什么新变化](3.12.html "下一章")

### 当前页

*   [报告 Bug](../bugs.html)
*   [显示源码](https://github.com/python/cpython/blob/main/Doc/whatsnew/3.13.rst)

«

### 导航

*   [索引](../genindex.html "总索引")
*   [模块](../py-modindex.html "Python 模块索引") |
*   [下一页](3.12.html "Python 3.12 有什么新变化") |
*   [上一页](3.14.html "What's new in Python 3.14") |
*   ![Python logo](../_static/py.svg)
*   [Python](https://www.python.org/) »

*   [3.14.0a1 Documentation](../index.html) »
*   [Python的新变化](index.html) »
*   Python 3.13 有什么新变化
*    
   
   |
*   Theme Auto Light Dark |

© [版权所有](../copyright.html) 2001 Python Software Foundation.  
This page is licensed under the Python Software Foundation License Version 2.  
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.  
See [History and License](/license.html) for more information.  
 
The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)  
 
最后更新于 11月 13, 2024 (05:41 UTC). [Found a bug](/bugs.html)?  
由 [Sphinx](https://www.sphinx-doc.org/) 8.1.3创建。