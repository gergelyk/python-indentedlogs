# indentedlogs

This library attempts to turn your logs into more readable form by addind
indentation to the messages according to their location in the call stack.
It also works well in conjunction with [coloredlogs](https://coloredlogs.readthedocs.io/en/latest/).

Let's see how these two libraries cooperate. As an example we will use
`demo.py` script.

??? note "demo.py"

    ```python
    def bump_version():
        pass


    def configure():
        log.debug(f"Collecting parameters")
        log.debug(f"Ask for confirmation")
        log.info(f"Save configuration")


    def select_target():
        log.warning(f"Default target selected")


    def prepare():
        log.debug(f"Bump version")
        bump_version()
        log.debug(f"Generate configuration")
        configure()
        log.debug(f"Select target")
        select_target()


    def call_compiler():
        log.debug(f"Preprocess sources")
        log.info(f"Compile sources")


    def call_linker():
        log.info(f"Link objects")


    def build_executable():
        # Note that callables that don't invoke logging
        # don't create additional indentation
        call_compiler()
        call_linker()


    def build_package():
        log.warning(f"Symbols will be removed")
        log.debug(f"Strip binary")
        log.debug(f"Add meta data")
        log.debug(f"Create archive")


    def upload_package():
        pass


    def release_app():
        log.debug(f"Prepare")
        prepare()
        log.info(f"Build executable")
        build_executable()
        log.info(f"Build package")
        build_package()
        log.info(f"Upload package")
        upload_package()


    release_app()
    ```

In order to make the script work, we need to obtain an instance of the logger and apply basic configuration. In the next step we will add indenting and coloring as demonstrated below.

```python  tab="Initial Configuration"
import logging



fmt = '{asctime} {levelname:<8} {filename:>3}:{lineno:<3} {name:>10} {message}'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level='DEBUG', format=fmt, datefmt=datefmt, style='{')

log = logging.getLogger()
```

```python hl_lines="2 8" tab="Indenting Added"
import logging
import indentedlogs


fmt = '{asctime} {levelname:<8} {filename:>3}:{lineno:<3} {name:>10} {message}'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level='DEBUG', format=fmt, datefmt=datefmt, style='{')
indentedlogs.install()
log = logging.getLogger()
```

```python hl_lines="3 6 7" tab="Coloring Added"
import logging
import indentedlogs
import coloredlogs

fmt = '{asctime} {levelname:<8} {filename:>3}:{lineno:<3} {name:>10} {message}'

coloredlogs.install(level='DEBUG', fmt=fmt, style='{')
indentedlogs.install()  # must be called after coloredlogs
log = logging.getLogger()
```

Finally we can run three versions of the script and compare the results. Note that the actual color palette may differ from the one below.

<div class="superfences-tabs">
<input id="__tab_2_0" name="__tabs_2" type="radio"/>
<label for="__tab_2_0">Initial Configuration</label>
<div class="superfences-content"><div class="codehilite"><pre><span></span><code>2020-04-07 19:33:28 DEBUG    demo.py:59        root Prepare
2020-04-07 19:33:28 DEBUG    demo.py:23        root Bump version
2020-04-07 19:33:28 DEBUG    demo.py:25        root Generate configuration
2020-04-07 19:33:28 DEBUG    demo.py:13        root Collecting parameters
2020-04-07 19:33:28 DEBUG    demo.py:14        root Ask for confirmation
2020-04-07 19:33:28 INFO     demo.py:15        root Save configuration
2020-04-07 19:33:28 DEBUG    demo.py:27        root Select target
2020-04-07 19:33:28 WARNING  demo.py:19        root Default target selected
2020-04-07 19:33:28 INFO     demo.py:61        root Build executable
2020-04-07 19:33:28 DEBUG    demo.py:32        root Preprocess sources
2020-04-07 19:33:28 INFO     demo.py:33        root Compile sources
2020-04-07 19:33:28 INFO     demo.py:37        root Link objects
2020-04-07 19:33:28 INFO     demo.py:63        root Build package
2020-04-07 19:33:28 WARNING  demo.py:48        root Symbols will be removed
2020-04-07 19:33:28 DEBUG    demo.py:49        root Strip binary
2020-04-07 19:33:28 DEBUG    demo.py:50        root Add meta data
2020-04-07 19:33:28 DEBUG    demo.py:51        root Create archive
2020-04-07 19:33:28 INFO     demo.py:65        root Upload package
</code></pre></div></div>
<input id="__tab_2_1" name="__tabs_2" type="radio"/>
<label for="__tab_2_1">Indenting Added</label>
<div class="superfences-content"><div class="codehilite"><pre><span></span><code>2020-04-07 19:33:28 DEBUG    demo.py:59        root Prepare
2020-04-07 19:33:28 DEBUG    demo.py:23        root   Bump version
2020-04-07 19:33:28 DEBUG    demo.py:25        root   Generate configuration
2020-04-07 19:33:28 DEBUG    demo.py:13        root     Collecting parameters
2020-04-07 19:33:28 DEBUG    demo.py:14        root     Ask for confirmation
2020-04-07 19:33:28 INFO     demo.py:15        root     Save configuration
2020-04-07 19:33:28 DEBUG    demo.py:27        root   Select target
2020-04-07 19:33:28 WARNING  demo.py:19        root     Default target selected
2020-04-07 19:33:28 INFO     demo.py:61        root Build executable
2020-04-07 19:33:28 DEBUG    demo.py:32        root   Preprocess sources
2020-04-07 19:33:28 INFO     demo.py:33        root   Compile sources
2020-04-07 19:33:28 INFO     demo.py:37        root   Link objects
2020-04-07 19:33:28 INFO     demo.py:63        root Build package
2020-04-07 19:33:28 WARNING  demo.py:48        root   Symbols will be removed
2020-04-07 19:33:28 DEBUG    demo.py:49        root   Strip binary
2020-04-07 19:33:28 DEBUG    demo.py:50        root   Add meta data
2020-04-07 19:33:28 DEBUG    demo.py:51        root   Create archive
2020-04-07 19:33:28 INFO     demo.py:65        root Upload package
</code></pre></div></div>
<input checked="checked" id="__tab_2_2" name="__tabs_2" type="radio"/>
<label for="__tab_2_2">Coloring Added</label>
<div class="superfences-content"><div class="codehilite"><pre><span></span><code><font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:59</font>        <font color="grey">root</font> <font color="green">Prepare</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:23</font>        <font color="grey">root</font>   <font color="green">Bump version</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:25</font>        <font color="grey">root</font>   <font color="green">Generate configuration</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:13</font>        <font color="grey">root</font>     <font color="green">Collecting parameters</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:14</font>        <font color="grey">root</font>     <font color="green">Ask for confirmation</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:15</font>        <font color="grey">root</font>     <font color="blue">Save configuration</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:27</font>        <font color="grey">root</font>   <font color="green">Select target</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">WARNING</font>  <font>demo.py:19</font>        <font color="grey">root</font>     <font color="darkorange">Default target selected</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:61</font>        <font color="grey">root</font> <font color="blue">Build executable</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:32</font>        <font color="grey">root</font>   <font color="green">Preprocess sources</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:33</font>        <font color="grey">root</font>   <font color="blue">Compile sources</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:37</font>        <font color="grey">root</font>   <font color="blue">Link objects</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:63</font>        <font color="grey">root</font> <font color="blue">Build package</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">WARNING</font>  <font>demo.py:48</font>        <font color="grey">root</font>   <font color="darkorange">Symbols will be removed</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:49</font>        <font color="grey">root</font>   <font color="green">Strip binary</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:50</font>        <font color="grey">root</font>   <font color="green">Add meta data</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">DEBUG</font>    <font>demo.py:51</font>        <font color="grey">root</font>   <font color="green">Create archive</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:65</font>        <font color="grey">root</font> <font color="blue">Upload package</font>
</code></pre></div></div>
</div>


`indentedlogs` determines indentation using indentation level, which is a measure of displacement. Followin rules apply while makeing indentations:

* Indentation level of the first message is always 0.
* Indentation level is calculated incrementaly from the relative position in the call stack.
* Methods/functions used for logging (by default all the methods of `logging.Logger` class) are discarded in the call stack.
* Indentation level can increase at most by 1 and decrease by any value between subsequent messages.
* Indentation level is rounded up to the nearest integer.
* Indentation level is coerced to 0..`max_level` range. Coercing from above the rane is indicated by special characters (by default `..`).

In order to see how the algorithm works, let's change logging level from `DEBUG` to `INFO`.

<div class="superfences-tabs">
<input id="__tab_3_0" name="__tabs_3" type="radio"/>
<label for="__tab_3_0">Initial Configuration</label>
<div class="superfences-content"><div class="codehilite"><pre><span></span><code>2020-04-07 19:33:28 INFO     demo.py:15        root Save configuration
2020-04-07 19:33:28 WARNING  demo.py:19        root Default target selected
2020-04-07 19:33:28 INFO     demo.py:61        root Build executable
2020-04-07 19:33:28 INFO     demo.py:33        root Compile sources
2020-04-07 19:33:28 INFO     demo.py:37        root Link objects
2020-04-07 19:33:28 INFO     demo.py:63        root Build package
2020-04-07 19:33:28 WARNING  demo.py:48        root Symbols will be removed
2020-04-07 19:33:28 INFO     demo.py:65        root Upload package
</code></pre></div></div>
<input id="__tab_3_1" name="__tabs_3" type="radio"/>
<label for="__tab_3_1">Indenting Added</label>
<div class="superfences-content"><div class="codehilite"><pre><span></span><code>2020-04-07 19:33:28 INFO     demo.py:15        root Save configuration
2020-04-07 19:33:28 WARNING  demo.py:19        root Default target selected
2020-04-07 19:33:28 INFO     demo.py:61        root Build executable
2020-04-07 19:33:28 INFO     demo.py:33        root   Compile sources
2020-04-07 19:33:28 INFO     demo.py:37        root   Link objects
2020-04-07 19:33:28 INFO     demo.py:63        root Build package
2020-04-07 19:33:28 WARNING  demo.py:48        root   Symbols will be removed
2020-04-07 19:33:28 INFO     demo.py:65        root Upload package
</code></pre></div></div>
<input checked="checked" id="__tab_3_2" name="__tabs_3" type="radio"/>
<label for="__tab_3_2">Coloring Added</label>
<div class="superfences-content"><div class="codehilite"><pre><span></span><code><font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:15</font>        <font color="grey">root</font> <font color="blue">Save configuration</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">WARNING</font>  <font>demo.py:19</font>        <font color="grey">root</font> <font color="darkorange">Default target selected</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:61</font>        <font color="grey">root</font> <font color="blue">Build executable</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:33</font>        <font color="grey">root</font>   <font color="blue">Compile sources</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:37</font>        <font color="grey">root</font>   <font color="blue">Link objects</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:63</font>        <font color="grey">root</font> <font color="blue">Build package</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">WARNING</font>  <font>demo.py:48</font>        <font color="grey">root</font>   <font color="darkorange">Symbols will be removed</font>
<font color="green">2020-04-07 19:33:28</font> <font color="dodgerblue">INFO</font>     <font>demo.py:65</font>        <font color="grey">root</font> <font color="blue">Upload package</font>
</code></pre></div></div>
</div>

Please check [API](api) documentation for the details on how to fine-tune the algorithm.
