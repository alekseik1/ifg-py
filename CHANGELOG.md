# CHANGELOG



## v2.2.2 (2024-05-23)

### Fix

* fix: permissions ([`6d2531a`](https://github.com/alekseik1/ifg-py/commit/6d2531afe7aed04be1ff192bb69a02a7df6be0e2))


## v2.2.1 (2024-05-23)

### Fix

* fix: release id ([`b8591c3`](https://github.com/alekseik1/ifg-py/commit/b8591c30e499e5ebb6f57893ca01a1649b4017f5))


## v2.2.0 (2024-05-23)

### Build

* build: release scripts ([`64453ed`](https://github.com/alekseik1/ifg-py/commit/64453edae7a031a7cc1618bf0ab46affa2a7f3e9))

* build: use fdint my own ([`6786a34`](https://github.com/alekseik1/ifg-py/commit/6786a34fa87ace5aeff7ecf4da223e8fe89511d3))

* build: lock poetry ([`e3694e3`](https://github.com/alekseik1/ifg-py/commit/e3694e31b7cc10dccba09e2795923d07a1a2a3ff))

* build: partial poetry ([`9f0c7a6`](https://github.com/alekseik1/ifg-py/commit/9f0c7a664ea014942636b83624122998319500a0))

* build(poetry): refactor deps ([`6c30138`](https://github.com/alekseik1/ifg-py/commit/6c3013862a0085c3f25536c865ece74854138c7c))

* build: update lock file for old poetry ([`0628081`](https://github.com/alekseik1/ifg-py/commit/06280816858b440cf414a2a5ba9384fe978af271))

* build: initial support for 3.12 ([`02e3698`](https://github.com/alekseik1/ifg-py/commit/02e369842114d566b061b483e25e3f550e1bd13b))

### Ci

* ci: conditional ([`75cc650`](https://github.com/alekseik1/ifg-py/commit/75cc65086fd685a855b7409a65a78d5470661938))

* ci: disable new installer on 2.7 ([`b3b51dc`](https://github.com/alekseik1/ifg-py/commit/b3b51dc3cd7c15aa302e244e1e033dad219d9702))

* ci: install numpy ([`fc8fc88`](https://github.com/alekseik1/ifg-py/commit/fc8fc883d4438184ef841d9defe88f264491101c))

* ci: fix ([`23e1396`](https://github.com/alekseik1/ifg-py/commit/23e1396764ff8ca34f1f1b4e73892e6f18bae4ff))

* ci: use container ([`d9c532f`](https://github.com/alekseik1/ifg-py/commit/d9c532fd00ae4c4aaccccff543a9d2832ffd4c4d))

* ci: add 3.10 ([`a3e6ad7`](https://github.com/alekseik1/ifg-py/commit/a3e6ad786f2a3888234628c48a152a847e36e974))

### Documentation

* docs: fix types ([`8792ca6`](https://github.com/alekseik1/ifg-py/commit/8792ca640ae7bcd7506a08c33a2aed46e2f4abe0))

### Feature

* feat: remove scipy dependency ([`0a4eb2c`](https://github.com/alekseik1/ifg-py/commit/0a4eb2cd4b0c12685b998df4b664c6fb3baa78c1))

### Fix

* fix: correct numpy order ([`b7a8233`](https://github.com/alekseik1/ifg-py/commit/b7a82337f345d18be9acd47af7e3a9163ea48ef3))

* fix: correct converter for python2 ([`610bb85`](https://github.com/alekseik1/ifg-py/commit/610bb850d04c581b42e4e37941364e5466b31e58))

### Test

* test: permissive test ([`6a82105`](https://github.com/alekseik1/ifg-py/commit/6a82105ce4f064b8f98cd597cb4c241aae191adf))

* test: rtol=1e-2 ([`c75d4ee`](https://github.com/alekseik1/ifg-py/commit/c75d4ee5a86b0dd5303ae24e109221c48fe0056c))

* test: rtol=1e-3 ([`6891362`](https://github.com/alekseik1/ifg-py/commit/6891362e8497322cec5fa1b6f9b54288489e80a9))

* test: fix rtol ([`8c084b6`](https://github.com/alekseik1/ifg-py/commit/8c084b69990ff13311761845e57bd25067ed0042))

* test: fix asymptotic tests ([`3291846`](https://github.com/alekseik1/ifg-py/commit/329184640e54d5a6fb7356964e7890b055cd1735))

* test: fix rtol ([`17da291`](https://github.com/alekseik1/ifg-py/commit/17da29167c8965b9b71ed59889879a646ab06065))

* test: fix np deprecation ([`8d8c936`](https://github.com/alekseik1/ifg-py/commit/8d8c936a5a5a144038ecae56c222a880c17b8eec))


## v2.1.1 (2021-09-27)

### Ci

* ci: remove venv caching in `examples` ([`69bd477`](https://github.com/alekseik1/ifg-py/commit/69bd477dcd2325cdbc462ff3d2835a6d224cdda8))

* ci: continue on flake8 errors ([`8ee2659`](https://github.com/alekseik1/ifg-py/commit/8ee2659901d95bfed1be1eec102d86cbdaec8ff9))

* ci: remove venv caching ([`aef65ca`](https://github.com/alekseik1/ifg-py/commit/aef65cae4aa0c0476ae893067fe83bcf85001332))

* ci: use `python -m` for pytest run ([`c95100f`](https://github.com/alekseik1/ifg-py/commit/c95100f8dbd043368f6fd97443f885c02790f330))

### Documentation

* docs(examples): fix examples ([`69edc7a`](https://github.com/alekseik1/ifg-py/commit/69edc7a00c5de3aee0cddc03dcaebe02d2a8d1be))

* docs(examples): add example for theta usage ([`fb8f094`](https://github.com/alekseik1/ifg-py/commit/fb8f094b504470f1fcf5c46a611e9556c5dda393))

### Fix

* fix(calculator): examples ([`b5a71ab`](https://github.com/alekseik1/ifg-py/commit/b5a71abb78d41cd8fe9a05460481107dcada3a9c))

* fix: flake errors ([`405eacf`](https://github.com/alekseik1/ifg-py/commit/405eacf3eab85bb5cf3f1be16b1c71e7203b2d19))

### Refactor

* refactor: expand kwargs to actual list, use ValueError instead of RuntimeError ([`6983bbf`](https://github.com/alekseik1/ifg-py/commit/6983bbf57f8afcc3377c14f63221f0ee83adb7d9))

* refactor: apply black + isort + docformatter ([`b422e72`](https://github.com/alekseik1/ifg-py/commit/b422e72651b0ec5d0e06febfe1b257e0349b1b61))

* refactor: remove redundant configs ([`995ed33`](https://github.com/alekseik1/ifg-py/commit/995ed33629bff87eac265d368d3354fc27e718fd))

### Test

* test: fix test errors ([`0568cc9`](https://github.com/alekseik1/ifg-py/commit/0568cc9a0c5815633730daaaf7132760bdf535b3))

### Unknown

* Merge pull request #36 from alekseik1/altinput

Extended input ([`886d57c`](https://github.com/alekseik1/ifg-py/commit/886d57ccfa4aebb2b6069ecbd716160539e43321))

* tests: fix tests ([`37cf9be`](https://github.com/alekseik1/ifg-py/commit/37cf9be807424e71980355f217f92a4fc37cd485))

* Extended input

Added arguments thetas, densities and rs besides temperatures and
volumes. All arguments to the constructor are named (kwargs). Added
arguments checking. Corrected examples.py and plots.
Parameter thetas is the ratio T/T_F. rs is the Brueckner parameter:
4./3. * \pi * r_s^3 = 1/n. ([`698e2c4`](https://github.com/alekseik1/ifg-py/commit/698e2c46b5c7fcd1a362453c4e7e104df847efcf))

* Merge pull request #35 from alekseik1/refactor/cleanup

refactor: remove redundant configs ([`e645567`](https://github.com/alekseik1/ifg-py/commit/e645567aa46e8aa26581b87f135972e9a384e315))


## v2.1.0 (2021-08-15)

### Chore

* chore(ci): remove codeQL scan ([`6ef7ccb`](https://github.com/alekseik1/ifg-py/commit/6ef7ccbf4dba7082964b60a2faef398954b7ed81))

* chore: apply black + isort + docformatter to __init__.py ([`569bd84`](https://github.com/alekseik1/ifg-py/commit/569bd8427587b3c4f34a8a460f538f1b71da5665))

### Feature

* feat(calculator): support for theta under vectorized volume ([`b94c591`](https://github.com/alekseik1/ifg-py/commit/b94c5912c66f5eb0423f70fc92a4a6a65635771a))

* feat(converter): support array volumes in theta ([`1029f72`](https://github.com/alekseik1/ifg-py/commit/1029f72876d57fea7ce2e94f1e643112ef2da7a8))

* feat(calculator): support for theta input ([`2de80dd`](https://github.com/alekseik1/ifg-py/commit/2de80dda9a7c6d23c8a7594c0bf7fe7aeb1575e5))

* feat(converter): converter from theta to temperatures ([`80531f5`](https://github.com/alekseik1/ifg-py/commit/80531f5dd18f36dc16e618280371cb88a7c747eb))

### Fix

* fix(calculator): match theta mesh dimensions with volume ones

Simply transpose array ([`94fa7e1`](https://github.com/alekseik1/ifg-py/commit/94fa7e1105b1a9cbc2956cc9587547029f616b71))

* fix(converter): make sure `volume` is not an array

For theta parameter support, volume should be a scalar, since otherwise we&#39;ll have to deal with 3-d matrix during `mu` calculation. For simplicity, the volume-as-array support is dropped ([`5eabaa5`](https://github.com/alekseik1/ifg-py/commit/5eabaa5ab249a5ee1dae820999f3d1e56f4b0914))

### Refactor

* refactor(tests): remove unused variable ([`41e1f18`](https://github.com/alekseik1/ifg-py/commit/41e1f1895c433d0b53fb85c8d9b9f03eb0f699f8))

### Test

* test(calculator): smoke test for theta input ([`91786a1`](https://github.com/alekseik1/ifg-py/commit/91786a17a5e2a3372a4cbd7c40602b01ba844213))

* test(calculator): `with_theta` call before volume input ([`4638754`](https://github.com/alekseik1/ifg-py/commit/4638754e313ed11f27729af08bf8e57402ac36da))

* test: more tests for mesh creation ([`95ccebb`](https://github.com/alekseik1/ifg-py/commit/95ccebb19760f08e8388469b6b9312f50c4fd89d))

* test: correct mesh creation + refactor theta to separate file ([`84b9ec3`](https://github.com/alekseik1/ifg-py/commit/84b9ec39e9f64a02f55d52ba77f3228b032df02d))

### Unknown

* Merge pull request #34 from alekseik1/feat/theta

theta parameter support ([`6a96e45`](https://github.com/alekseik1/ifg-py/commit/6a96e452beb69e056be0d62876842d5d2b937343))

* doc(converter): inform that volume should be in atomic ([`a55309d`](https://github.com/alekseik1/ifg-py/commit/a55309d36d98cfcdee71d903077b53de1aab10a7))


## v2.0.0 (2021-08-13)

### Breaking

* feat(calculator): builder interface for calculator

WIP, also needs doc updates

BREAKING CHANGE: breaks previous input interface ([`95e96c6`](https://github.com/alekseik1/ifg-py/commit/95e96c64f733316e576322f63193306ad5c85105))

### Build

* build: only build whl package ([`ab0fd1f`](https://github.com/alekseik1/ifg-py/commit/ab0fd1f58901aed5a1ed2b694cf1dade03a7fb58))

### Chore

* chore: fix poetry build ([`56e05fc`](https://github.com/alekseik1/ifg-py/commit/56e05fc5eee360aa1485c6c3d7fe62ce5328282e))

* chore: get rid of setup.py ([`4aef428`](https://github.com/alekseik1/ifg-py/commit/4aef428877e9276d91968b1935eb88464667e55c))

* chore(ci): introduce code coverage ([`3cbac5b`](https://github.com/alekseik1/ifg-py/commit/3cbac5b8c5f47a29c6d301db7a76ceaa56dce70f))

* chore(pyproject): add pytest-cov ([`85753d9`](https://github.com/alekseik1/ifg-py/commit/85753d92fd29b5435e38e5f2086245a220498daa))

* chore(ci): rename examples pipeline ([`98fa5c8`](https://github.com/alekseik1/ifg-py/commit/98fa5c8f293a01a20a6744d90f404a36aa436567))

* chore(pyproject): add black, isort, docformatter and update requirements ([`0183a50`](https://github.com/alekseik1/ifg-py/commit/0183a508739105b037a6e30606dc9c2dd3c014d0))

* chore(ci): remove coverage block ([`f4f6467`](https://github.com/alekseik1/ifg-py/commit/f4f64672490949d6a4c1cc009fbf94e2073f0daf))

* chore(ci): remove pip instruction ([`dcdd3a7`](https://github.com/alekseik1/ifg-py/commit/dcdd3a79e48f53a237170883aa6488b15b99b0cf))

* chore(ci): don&#39;t build against py2.7 on macos ([`40fbef3`](https://github.com/alekseik1/ifg-py/commit/40fbef3483bb38f8214259cb981fa282c5bbab08))

* chore(ci): install numpy in advance ([`efa34d3`](https://github.com/alekseik1/ifg-py/commit/efa34d3186336dd6696084a553a7e8a06797eb78))

* chore(ci): test on macOS ([`e99354d`](https://github.com/alekseik1/ifg-py/commit/e99354d0fe7ef552eb1c0fc081bba2feb72a948f))

* chore(poetry): properly specify versions for old pythons ([`9bb020f`](https://github.com/alekseik1/ifg-py/commit/9bb020f0cbea41ac803fa81254e90492079421ea))

* chore(pyproject): drop support for Python 3.5 ([`0e0adeb`](https://github.com/alekseik1/ifg-py/commit/0e0adebaf7b4652099a1e774e9e7069150c2cb17))

* chore(ci): don&#39;t reinstall deps if cache is hit ([`12339cf`](https://github.com/alekseik1/ifg-py/commit/12339cf206b5196b4c6c222d194934d135c8f31d))

* chore(ci): fix examples pipeline ([`9b30384`](https://github.com/alekseik1/ifg-py/commit/9b303844299792c8be15ae15741c901c4222a5ee))

* chore(flake): ignore .venv created during pipeline ([`74037df`](https://github.com/alekseik1/ifg-py/commit/74037dfd6a34a4f0de222ae8af7fd0ad1eabc9ec))

* chore(ci): clean up pipeline ([`625ae65`](https://github.com/alekseik1/ifg-py/commit/625ae65e74e35f4965b54b151f51864153badee7))

* chore(ci): test only on Ubuntu ([`1422c61`](https://github.com/alekseik1/ifg-py/commit/1422c6197f294b839ec1e986d462aee2e33b3c48))

* chore(ci): install Fortran compiler on macOS ([`75d24c8`](https://github.com/alekseik1/ifg-py/commit/75d24c8ad610d0ec298f35a5b30dceaa9037be15))

* chore(ci): remove Windows builds ([`662cb42`](https://github.com/alekseik1/ifg-py/commit/662cb426a9e3da4644af9ffcc44b83f9ee4d8bca))

* chore(ci): drop py3.8 on Windows tests ([`170c7fe`](https://github.com/alekseik1/ifg-py/commit/170c7fe0bfe1fb29e6e304013eee3f0dd2b0ca83))

* chore(ci): don&#39;t specify MS VC++ version ([`b6f3a19`](https://github.com/alekseik1/ifg-py/commit/b6f3a19cc8929f20e1b04a2b1dee3d01eae0ab35))

* chore(ci): use poetry in install and test ([`c23b446`](https://github.com/alekseik1/ifg-py/commit/c23b4466297ff8ace632750c4fa68e87fa272247))

* chore(ci): attempt to fix versions ([`cceeea2`](https://github.com/alekseik1/ifg-py/commit/cceeea2b737697225a4527f38030073b775d43b7))

* chore(ci): specify 3.5.10 ([`9205c34`](https://github.com/alekseik1/ifg-py/commit/9205c34032ac32c830e0dfeba54c83459e0bf21c))

* chore(ci): fix ident ([`27793cb`](https://github.com/alekseik1/ifg-py/commit/27793cb05d4e5dbe7280c593860b1cb223952e92))

* chore(ci): export poetry to requirements.txt ([`2a9729f`](https://github.com/alekseik1/ifg-py/commit/2a9729fed4ff0e351811c658cad71c44e26f7cb2))

* chore(ci): comment out unsupported params ([`3a4ef9d`](https://github.com/alekseik1/ifg-py/commit/3a4ef9d721f43889a671319918ae303208b7ab73))

* chore(ci): another GH Action for Poetry ([`dfdea46`](https://github.com/alekseik1/ifg-py/commit/dfdea462b3a7256c9183a9078dac52bae83d9906))

* chore(poetry): lock poetry.lock ([`06b2419`](https://github.com/alekseik1/ifg-py/commit/06b241977646059b0818574d04f910099fc097c8))

* chore(ci): separate pipeline for examples ([`4fd13f9`](https://github.com/alekseik1/ifg-py/commit/4fd13f927bd9a244412cd42d1640ac5a5232842c))

* chore(ci): cache poetry venv ([`bc12f5e`](https://github.com/alekseik1/ifg-py/commit/bc12f5e794b1316783f6e4bd4688108f3abc8e8d))

* chore(poetry): move matplotlib to dev dependencies ([`a17260b`](https://github.com/alekseik1/ifg-py/commit/a17260b1ab612ab87cf898695eb761f722cc80cb))

* chore(ci): lock poetry in pipeline ([`e818c80`](https://github.com/alekseik1/ifg-py/commit/e818c80117d770842a25f9ed0daee2d8c797cd0c))

* chore(poetry): update matplotlib deps ([`77645e5`](https://github.com/alekseik1/ifg-py/commit/77645e5d96088b98e7ef37d5e61b7d1b337419b3))

* chore(poetry): initial dependencies setup ([`c07386d`](https://github.com/alekseik1/ifg-py/commit/c07386d7b0cd84aad6e4c3afdaaad6b8f3eb8586))

* chore(ci): use poetry in CI ([`37fe5bb`](https://github.com/alekseik1/ifg-py/commit/37fe5bbadc6968f115bbb93ede25ff37a36b57d0))

* chore(pyproject): initial poetry setup ([`e3a01f8`](https://github.com/alekseik1/ifg-py/commit/e3a01f8c545ec5f8e6a0cb02dcf8b3504153eadb))

* chore(ci): test against py3.8 and py3.9 ([`1e99937`](https://github.com/alekseik1/ifg-py/commit/1e99937f1229f04f2d14a31b9366c424de337268))

* chore(ci): remove tests on py2.7 with Windows OS ([`6da822f`](https://github.com/alekseik1/ifg-py/commit/6da822fe6e599fc046e117f0379030c7c9f69c75))

* chore(ci): remove tests on py2.7 with Windows OS ([`00823fa`](https://github.com/alekseik1/ifg-py/commit/00823fae8a023c0cfc281a4b35d2c2e2eb4843a6))

* chore(ci): specify msvc version (2) ([`43573c6`](https://github.com/alekseik1/ifg-py/commit/43573c60a36ed462b897eb211627590d1bfcc5ac))

* chore(ci): specify msvc version ([`28eb040`](https://github.com/alekseik1/ifg-py/commit/28eb0403d9a703549a0da8a56813fc5e0e7d0ef4))

* chore(ci): set up MS Visual C++ for Windows ([`a60f5a4`](https://github.com/alekseik1/ifg-py/commit/a60f5a40b4c722cd7583f57cf0f52254c3a08d91))

* chore(ci): don&#39;t use bash syntax in pipeline

This fixes crashes on Windows build ([`cd9a0c5`](https://github.com/alekseik1/ifg-py/commit/cd9a0c50e68f62ee378599b1e07724925228cb15))

* chore(ci): test against different operating systems

These systems are MacOS, Ubuntu and Windows ([`a8e4d45`](https://github.com/alekseik1/ifg-py/commit/a8e4d453fd9e85cd9f546dc8b464fef8840b667c))

* chore(ci): enable daily builds ([`2e4d911`](https://github.com/alekseik1/ifg-py/commit/2e4d9114b83a72c85adb4e16c6733f085655d194))

### Documentation

* docs(calculator): comment with r_s formula ([`80ef695`](https://github.com/alekseik1/ifg-py/commit/80ef695f025dd08d0a0f70fe19d83188f80668ef))

* docs(calculator): IfgCalculation class documentation ([`d1271a2`](https://github.com/alekseik1/ifg-py/commit/d1271a27d85da4027ac5ec3108b51f51e955b778))

* docs(readme): correct badges ([`7286fd5`](https://github.com/alekseik1/ifg-py/commit/7286fd54bf58038cc58d577f7a771774339f72b0))

* docs(readme.md): add codecov status ([`ca42075`](https://github.com/alekseik1/ifg-py/commit/ca4207501669e63ae824010007229371213240f7))

* docs(ci): comments for stages ([`8e826a3`](https://github.com/alekseik1/ifg-py/commit/8e826a357208a6921c425b2b132ee4366c34d616))

* docs: Merge pull request #24 from alekseik1/comment

Corrected usage instructions in __init__.py ([`c009389`](https://github.com/alekseik1/ifg-py/commit/c00938994daa747a80f2a85d135a5621f6758558))

### Feature

* feat(calculator): support for r_s (WIP)

Needs tests ([`7322936`](https://github.com/alekseik1/ifg-py/commit/73229363713f1603f6821217ef46207567e2c170))

### Fix

* fix: use gbar as property

This prevents forgetful users from not updating gbar after g/mass updates ([`94dac3a`](https://github.com/alekseik1/ifg-py/commit/94dac3ae6157cb5faaab11dc5a727010efdd6b77))

* fix(calculator): tests for required parameters

Make sure they are specified before accessing any of properties ([`7a059d7`](https://github.com/alekseik1/ifg-py/commit/7a059d73d3281b305abf0e9b99e9045c00471dbd))

* fix(examples): correct calculator creation ([`723fdf0`](https://github.com/alekseik1/ifg-py/commit/723fdf0272e6e800e08d264bf3358482a691ef47))

### Refactor

* refactor: rebase ([`1d15998`](https://github.com/alekseik1/ifg-py/commit/1d1599828fe40b9cff4b0345fa18efc27b1db0d3))

### Style

* style: apply black + isort + docformatter ([`24f51e2`](https://github.com/alekseik1/ifg-py/commit/24f51e2fa7b4f582557612ed362503de990b6379))

* style(tests): line length in conftest ([`28939a5`](https://github.com/alekseik1/ifg-py/commit/28939a51b04653883ff2cec07e0fedcc7691765e))

### Test

* test(converter): test for r_s to specific volume ([`6cc15ca`](https://github.com/alekseik1/ifg-py/commit/6cc15ca747011b48fd541c961211b6a358717630))

### Unknown

* Merge pull request #33 from alekseik1/feat/r_s

Fixes after paper review ([`c6e7231`](https://github.com/alekseik1/ifg-py/commit/c6e723105945678d6c13334eadd1320fd4c810a5))

* Merge pull request #31 from alekseik1/chore/codeql_scan

Create codeql-analysis.yml ([`1a0f6fa`](https://github.com/alekseik1/ifg-py/commit/1a0f6fad8d0c96a17fff25c47d3746307b09f23c))

* Create codeql-analysis.yml ([`f2813ea`](https://github.com/alekseik1/ifg-py/commit/f2813eae7ee9eb71f0af7adf15599f2c212179d4))

* Merge pull request #30 from alekseik1/fix/stability

Fix/stability ([`ffc94db`](https://github.com/alekseik1/ifg-py/commit/ffc94dbaf665ac8963e35ba9448254faf013385b))

* revert: Revert &#34;chore(ci): another GH Action for Poetry&#34;

This reverts commit dfdea462b3a7256c9183a9078dac52bae83d9906. ([`43b0296`](https://github.com/alekseik1/ifg-py/commit/43b029645db89c518e3b3d552f91eef934874aed))

* Corrected usage instructions in __init__.py ([`0dfe8a9`](https://github.com/alekseik1/ifg-py/commit/0dfe8a94afcd042f492cb1c654558186ed786ed0))


## v1.2.0 (2021-01-07)

### Ci

* ci: make flake8 check obligatory ([`c696129`](https://github.com/alekseik1/ifg-py/commit/c69612935010246eef601aa82670526a0bd7ce0e))

### Documentation

* docs(README.md): add badge for tests ([`e22209f`](https://github.com/alekseik1/ifg-py/commit/e22209ff729a423d54e5d6ca975b792699c0e6aa))

* docs: add GitHub Actions build status ([`06dea65`](https://github.com/alekseik1/ifg-py/commit/06dea6551abe26c3be1decd6dce5e9aa8d098e56))

### Feature

* feat: correct get_all_properties ([`2c65491`](https://github.com/alekseik1/ifg-py/commit/2c6549118dc4c30536764af527e6eb3bef058e4e))

### Fix

* fix: python2.7 crash on `exist_ok` ([`44fbde5`](https://github.com/alekseik1/ifg-py/commit/44fbde5601c5d58657d42081dc227b2ed4dd8bf0))

### Style

* style: cleanup code ([`185cfb6`](https://github.com/alekseik1/ifg-py/commit/185cfb63386d3260f373eafb6e589f86957f0dfc))

### Test

* test: set default deadline to 5 seconds ([`b632163`](https://github.com/alekseik1/ifg-py/commit/b6321635eeca5eb476bb646d660a34219341b532))

### Unknown

* Merge pull request #23 from alekseik1/feat/get_all_properties

feat: correct get_all_properties ([`1e7566c`](https://github.com/alekseik1/ifg-py/commit/1e7566c4c10d2efee0a79dd1aa9885e912d17c7d))

* Merge pull request #22 from alekseik1/style/cleanup

Style/cleanup ([`8178553`](https://github.com/alekseik1/ifg-py/commit/8178553068a521b0749d22f9146fa3bb68ece42a))

* Merge pull request #21 from alekseik1/tests/timeout

test: set default deadline to 5 seconds ([`5776625`](https://github.com/alekseik1/ifg-py/commit/5776625b6386feaa1738f8af755a244702c22bf8))


## v1.1.0 (2021-01-07)

### Build

* build(setup.cfg): update settings ([`ca24ad1`](https://github.com/alekseik1/ifg-py/commit/ca24ad19c88c69b7b3ebba98244a90c5a1c257c5))

* build(setup.cfg): upload to PyPi ([`8393d82`](https://github.com/alekseik1/ifg-py/commit/8393d82e664e99c35b9411c589d4faae56be4a8b))

* build: increase version ([`72c3305`](https://github.com/alekseik1/ifg-py/commit/72c3305bf627e169d893b335bb4b2d24d90db2c8))

* build: move to semantic versioning ([`38b5a9f`](https://github.com/alekseik1/ifg-py/commit/38b5a9f239c05bfc02ab257d9ae4ae22905e969a))

* build: update version ([`e3798df`](https://github.com/alekseik1/ifg-py/commit/e3798dfe0765465f232f15907f493f541b8eb124))

* build: cache docker images ([`4f503e4`](https://github.com/alekseik1/ifg-py/commit/4f503e4b65cdf3f330e906ac1109c3a3c11fc913))

* build: use docker for installation tests ([`173e417`](https://github.com/alekseik1/ifg-py/commit/173e41747004522846d2a41122c217a3c064e40d))

* build: install package in separate virtual environment ([`79f2811`](https://github.com/alekseik1/ifg-py/commit/79f281126fdeb9d22fbf3c668e5727396fa607ae))

* build: use CI number as version postfix ([`fe60fab`](https://github.com/alekseik1/ifg-py/commit/fe60fab4e0739e021cb176ff350807fdac62b8eb))

* build: remove `setup_requires` ([`e681e1d`](https://github.com/alekseik1/ifg-py/commit/e681e1dd324934078bf8d4fe17f00099f7989ae2))

* build: don&#39;t use docker ([`1009c4d`](https://github.com/alekseik1/ifg-py/commit/1009c4d4a9c5bad3ef0ad2cd93dbe36394f6dcd2))

* build: no prompt for `pip uninstall` ([`04b8055`](https://github.com/alekseik1/ifg-py/commit/04b805512091f67ae42d98371268f70c70094295))

* build: tests for build ([`ee65b0a`](https://github.com/alekseik1/ifg-py/commit/ee65b0a353dfa25fab565187b57ad26276f2ccf6))

* build: fix jobs ([`1f16cfb`](https://github.com/alekseik1/ifg-py/commit/1f16cfba3d54aab4f4edf182ca445c953d87d618))

* build: use build jobs ([`3e5ccf6`](https://github.com/alekseik1/ifg-py/commit/3e5ccf6bf64971cb8d7b0ee369239f635b492768))

* build: different python versions in build matrix ([`631ef5a`](https://github.com/alekseik1/ifg-py/commit/631ef5ab937ed91b5e61fcd02f6f596caa680aaa))

* build: fix build config ([`611d560`](https://github.com/alekseik1/ifg-py/commit/611d560f5f738ac14af7082438f2a6efc59f8009))

* build: optimize tox config ([`9d26cd3`](https://github.com/alekseik1/ifg-py/commit/9d26cd3062868c6429796fd4f3d4a07ca9615742))

* build: update version ([`5db7dcd`](https://github.com/alekseik1/ifg-py/commit/5db7dcdad74b49f34328cdfae318c42fe2361921))

* build: remove `setup_requires` section
build: add classifiers for all supported python versions ([`b7dd489`](https://github.com/alekseik1/ifg-py/commit/b7dd489113ecd9ec52fddcd690eccc1150ba6254))

* build: increase version ([`c728072`](https://github.com/alekseik1/ifg-py/commit/c7280724384831c53fab203773993912bec27817))

* build: remove obsolete `sudo` directive ([`5d981ea`](https://github.com/alekseik1/ifg-py/commit/5d981ea927a034ef5f439fc14ae4bbcc1138aabb))

* build: version update ([`54208f6`](https://github.com/alekseik1/ifg-py/commit/54208f6d473bd342c02ca017779de53a7f99da68))

* build: increase version ([`b6214ba`](https://github.com/alekseik1/ifg-py/commit/b6214bacd01df71c30692c436ef185e05bcd33c7))

* build: add exception for docs build script ([`917e8be`](https://github.com/alekseik1/ifg-py/commit/917e8bec15dae84849abb4191cb12e3547bbd708))

* build: flake for Travis ([`9eccca8`](https://github.com/alekseik1/ifg-py/commit/9eccca89220ad3a04f5a8ba3d4987c9ff7b94e0c))

* build: explicitly mark &#39;twine&#39; version (bug in travis) ([`7eab9c3`](https://github.com/alekseik1/ifg-py/commit/7eab9c3fce335680eb85ca3600714040c09ffbb4))

* build: add Travis CI ([`8b1b6ac`](https://github.com/alekseik1/ifg-py/commit/8b1b6ac5f59e2dc21231cb49860445cf816e827a))

* build: increase version ([`c0eab75`](https://github.com/alekseik1/ifg-py/commit/c0eab7547e09d8f3d964941674802d046ba8ed83))

* build: increase version ([`3d9ac4b`](https://github.com/alekseik1/ifg-py/commit/3d9ac4b9da99d72b05066c8b4fb146f4327f1f35))

* build: setup tools for PyPi ([`efb0666`](https://github.com/alekseik1/ifg-py/commit/efb0666960604948f24f3d5e7ab2ab61dc68cc08))

### Ci

* ci(deploy.yml): fix semantic release ([`87d48fe`](https://github.com/alekseik1/ifg-py/commit/87d48fe6f186e66b0f98d6d00d20d5a061a7a308))

* ci(deploy): use semantic release Github Action ([`c5a1581`](https://github.com/alekseik1/ifg-py/commit/c5a1581b1b19164b48743f2920ad74adbc7bb511))

* ci: fix conditions ([`1321575`](https://github.com/alekseik1/ifg-py/commit/132157507171fbb6cc99a5a1db53e4c0af449f2b))

* ci: split build and deploy into two pipelines ([`4e94027`](https://github.com/alekseik1/ifg-py/commit/4e94027b94c261bf93602f7c0aa7f7c78c61102a))

### Documentation

* docs: icon for CI status ([`f2b9e1d`](https://github.com/alekseik1/ifg-py/commit/f2b9e1df974353333244f739c4a3d67bb47f65fc))

* docs: fix sphinx warnings ([`b9b4250`](https://github.com/alekseik1/ifg-py/commit/b9b42500d479dc3699e6e3b2addb2b84abbfea52))

* docs: add missing empty line ([`06a475a`](https://github.com/alekseik1/ifg-py/commit/06a475ad9a9c51a77ffa4803eb574dce4ff721d6))

* docs: basic readme ([`b3b0914`](https://github.com/alekseik1/ifg-py/commit/b3b0914a0148f6f1027fc67e7c51f77756afef08))

* docs: add sphinx files ([`e9938db`](https://github.com/alekseik1/ifg-py/commit/e9938dbf229e60db6e09fe38e13d3b3c5a81f094))

* docs: documentation for `units_converter` ([`515f389`](https://github.com/alekseik1/ifg-py/commit/515f389f60298b4703af687d9dab91b916e849ae))

### Feature

* feat: add energy to calculator ([`8cf1e7a`](https://github.com/alekseik1/ifg-py/commit/8cf1e7a4f9d7bc16121d656ad1e71863199905a0))

* feat: add plots examples ([`c5d2839`](https://github.com/alekseik1/ifg-py/commit/c5d2839995f2489902bfb6ceb075c8472c28218c))

* feat: get rid of pandas dependency ([`669b1a8`](https://github.com/alekseik1/ifg-py/commit/669b1a8da5e21db1a43f45c67c7f154cd22c2f6f))

* feat: declare support py&gt;=2.7 ([`ce3be6b`](https://github.com/alekseik1/ifg-py/commit/ce3be6bfecbff77a80be121fe5e3535952a64e5a))

* feat: `tox` framework ([`4d9b2a5`](https://github.com/alekseik1/ifg-py/commit/4d9b2a57f16558674a81851e5c95a21cac3133e4))

* feat: flake8 linter ([`9b4fd60`](https://github.com/alekseik1/ifg-py/commit/9b4fd60491e88d7fe42b1be4aacd8b6d2d5921a5))

* feat: class for all calculations ([`1477444`](https://github.com/alekseik1/ifg-py/commit/1477444bcd8e4a89d0cad1f0b65f73188def8a12))

* feat: `get_all_properties` with dumping to csv file
feat: `get_metal_specific_volume` -- &#39;v&#39; in atomic units
ref: small cleanup ([`6872a53`](https://github.com/alekseik1/ifg-py/commit/6872a53e87e55634ea1a9f0fd3952397fa2d5e5a))

* feat: save to csv file;
feat: add Copper to examples; ([`7bfa530`](https://github.com/alekseik1/ifg-py/commit/7bfa5301161391efc421cdda7c684b5a03c2709c))

* feat: ndarray in `get_sound_speed_entropy` ([`dd206f8`](https://github.com/alekseik1/ifg-py/commit/dd206f8bed103333b9ef9e6a9410c2ca03108ef6))

* feat: ndarray in `get_sound_speed_temperature` ([`2c46447`](https://github.com/alekseik1/ifg-py/commit/2c464475db64ccc1b0c0f53c8273f8e442153e9d))

* feat: ndarray in `get_heat_capacity_pressure` ([`5876160`](https://github.com/alekseik1/ifg-py/commit/58761608aaceadf8dbf78adc6e6f8a173ee4318c))

* feat: ndarray in `get_heat_capacity_volume` ([`51ed0d8`](https://github.com/alekseik1/ifg-py/commit/51ed0d85ada56578dd436998fe9c4baf59a55475))

* feat: ndarray in `get_entropy` ([`e44badc`](https://github.com/alekseik1/ifg-py/commit/e44badcf6b44392e3e404a3e783e25c1152881c5))

* feat: ndarray in `get_pressure` ([`7c0585c`](https://github.com/alekseik1/ifg-py/commit/7c0585c509a1054133fdab9101ee5c0423bd3e06))

* feat: ndarray in `get_F_potential` ([`9b5f9d0`](https://github.com/alekseik1/ifg-py/commit/9b5f9d08b38017626d57912d61d6eea027ec7fdb))

* feat: ndarray in `get_chemical_potential` ([`d918b46`](https://github.com/alekseik1/ifg-py/commit/d918b46548178e78cd23322f8d35fc01cb7c97be))

* feat: accept *args and **kwargs (just ignore them) ([`091ae08`](https://github.com/alekseik1/ifg-py/commit/091ae085d78dc42dcf84852ad81ab30e2b52ae96))

* feat: plot mu from T ([`296b8c4`](https://github.com/alekseik1/ifg-py/commit/296b8c40095b123c1e4220b2581f887d3ed1c869))

* feat: prettify graph visualizer ([`9a5388b`](https://github.com/alekseik1/ifg-py/commit/9a5388b2d3e1b46a7a5108a395aa51cd87dbf65b))

* feat: add grid to plots ([`2d8e880`](https://github.com/alekseik1/ifg-py/commit/2d8e880f48d953f4ac42bf7e7ed773d8516217c2))

* feat: example ([`2c1e161`](https://github.com/alekseik1/ifg-py/commit/2c1e161eedb32dd1a48df69352c3bd8c5430534a))

* feat: converter from density to specific volume in SI ([`8492a3c`](https://github.com/alekseik1/ifg-py/commit/8492a3cd3b6f17bb16f733d332ed67db71d48c10))

* feat: entropy, heat capacity and sound speed convert ([`1a85503`](https://github.com/alekseik1/ifg-py/commit/1a85503567e91e25ec0532a78ab8f5912ad137de))

* feat: convert for volume and pressure ([`e0a24f3`](https://github.com/alekseik1/ifg-py/commit/e0a24f31d4058066968baad4d569fec87d4dc8e8))

* feat: units converter. Energy and temperature only ([`660ae0e`](https://github.com/alekseik1/ifg-py/commit/660ae0ee06eb0091d73cd90c6a7619a867642caa))

* feat: calculator for atomic units ([`54c946b`](https://github.com/alekseik1/ifg-py/commit/54c946bafb18021a6a7055665ea8e6a7f57dc8bd))

### Fix

* fix(setup.cfg): syntax quotes ([`d6b45bf`](https://github.com/alekseik1/ifg-py/commit/d6b45bf90f44d3acaea7d706b8db0ce3db2833d6))

* fix: increase version ([`da8920f`](https://github.com/alekseik1/ifg-py/commit/da8920fa0a9f966b3ee92a179092f4087f6d7bb1))

* fix: p -&gt; P in `get_all_properties` ([`a420a50`](https://github.com/alekseik1/ifg-py/commit/a420a50160b02753db1491ec27c14ed7302115e5))

* fix: duplicate classifiers ([`aafbeef`](https://github.com/alekseik1/ifg-py/commit/aafbeef927ad22a15ad9eab37432ccb6941d2525))

* fix: better threshold value for low-temperature limits ([`d406b9a`](https://github.com/alekseik1/ifg-py/commit/d406b9a337aeb1218704895d82edbb6cd0396c4d))

* fix: hypothesis warnings ([`5f96a7d`](https://github.com/alekseik1/ifg-py/commit/5f96a7dc0011565cde53b43981ef8c5f95659231))

* fix: syntax for py=2.7 in tests ([`c2a16b2`](https://github.com/alekseik1/ifg-py/commit/c2a16b2a763cdd60d74ecb9b8cd32a973d98f851))

* fix: precision problem on low temperatures ([`9e2b83d`](https://github.com/alekseik1/ifg-py/commit/9e2b83d7534f62b880d91cd66a0900e8cb6b2986))

* fix: mistype in low temp test for C_S ([`887a800`](https://github.com/alekseik1/ifg-py/commit/887a80007a8dabb95073fddb50ff58f391075f17))

* fix: change numpy assert functions to `assert_allclose` since they are more stable ([`47e3939`](https://github.com/alekseik1/ifg-py/commit/47e3939289494a8085d39343ecd3905034301fa8))

* fix: get rid of hypothesis since it is broken for py2.7 ([`b2d54de`](https://github.com/alekseik1/ifg-py/commit/b2d54dedcaa51fb58d0846366325463591d40671))

* fix: true division for py&lt;3 ([`07049b9`](https://github.com/alekseik1/ifg-py/commit/07049b99e93fca042d5f1e1801750e425758b216))

* fix: less RAM consumption ([`d18dd8d`](https://github.com/alekseik1/ifg-py/commit/d18dd8da9b0b0d554207379742d72fc5d540c012))

* fix: python2.7 compatibility ([`dc41ab9`](https://github.com/alekseik1/ifg-py/commit/dc41ab913dadfa94493f0ec4f243bbd81301c42e))

* fix: incorrect converter ([`a1bbd76`](https://github.com/alekseik1/ifg-py/commit/a1bbd76aee29a899a8c51dab130fe658ca5e83dc))

* fix: cast to np.array ([`9b6c526`](https://github.com/alekseik1/ifg-py/commit/9b6c5268e49fc32b390ffd4551a16ec4ede174dd))

* fix: fix incorrect power in fdk (float division on python2.*) ([`d7b5194`](https://github.com/alekseik1/ifg-py/commit/d7b519450aeb80e80d4da9b69c7a9dc7a64c0a33))

* fix: type annotation for python2.7 ([`0bf065f`](https://github.com/alekseik1/ifg-py/commit/0bf065fb1a6eee06da68328587b51dfa371f83cb))

* fix: typo in convert variable ([`64201aa`](https://github.com/alekseik1/ifg-py/commit/64201aa212dfcd05ace4dd8b6842fb6b17a486fd))

* fix: support for py&gt;=3.5 ([`26336ee`](https://github.com/alekseik1/ifg-py/commit/26336ee9b62ae0129d2f2e98c5f521190f5d18b2))

* fix: remove saving data in examples.py ([`58788f3`](https://github.com/alekseik1/ifg-py/commit/58788f3db3dddfda75f700f036dc8215de11800e))

* fix: flake8 errors ([`f9ff175`](https://github.com/alekseik1/ifg-py/commit/f9ff175a89f5328c43a2c9eeac81926f8b449740))

* fix: early import crash in both `setup.py` and `conf.py` ([`b5ac91f`](https://github.com/alekseik1/ifg-py/commit/b5ac91f43dad2ac4c6e45e2525ce76515f8ae2b9))

* fix: `setup` script crash because of early imports ([`d58a8bc`](https://github.com/alekseik1/ifg-py/commit/d58a8bc89fcad0c3953ed0d7aed630f9b3bf8cd9))

* fix: `setup_requires` ([`3ce66ab`](https://github.com/alekseik1/ifg-py/commit/3ce66abc93e4ade36bc3c9d7142540c0b282865c))

* fix: remove redundant dependencies ([`89ae6f2`](https://github.com/alekseik1/ifg-py/commit/89ae6f21808d3077f6dd8a6bd0387e11cee4ff0e))

* fix: install dependencies ([`6338e91`](https://github.com/alekseik1/ifg-py/commit/6338e91e0d0f36745a0fa3002014b600274a03e0))

* fix: mark as for Python&gt;=3.6 ([`f4b4c9b`](https://github.com/alekseik1/ifg-py/commit/f4b4c9bb9eb14cb3bffd09c97c33217d304cafaa))

* fix: broken examples ([`273aa89`](https://github.com/alekseik1/ifg-py/commit/273aa893560d35b6cd7dea3b26e4d15f55628531))

* fix: `get_metal_specific_volume` returns values in SI ([`6091c63`](https://github.com/alekseik1/ifg-py/commit/6091c63edd735557de84f4a11d41ba5ca18b9fbf))

* fix: missing documentation for functions in `units_converter.py` ([`e8bf0c1`](https://github.com/alekseik1/ifg-py/commit/e8bf0c1e515029282aaff6e63e4e1597fe298788))

* fix: pass *args and **kwargs to _fdk ([`7ab53d5`](https://github.com/alekseik1/ifg-py/commit/7ab53d597c6324faf34a44d38c85d4e90afef9b6))

* fix: warn about one parameter as vector problem ([`a2dc37f`](https://github.com/alekseik1/ifg-py/commit/a2dc37f8e2dcecbe15c1f7df474bbd770176a8c2))

* fix: specify package version in `__init__.py` ([`a78b82f`](https://github.com/alekseik1/ifg-py/commit/a78b82f6370544fc3c72d7ec249c1fae0d385be7))

* fix: conflict of `master_doc` on local machine and RTD ([`ec53a35`](https://github.com/alekseik1/ifg-py/commit/ec53a352762476efa85eef610ad3b3c54844ce9b))

* fix: explicitly import functions ([`1c19166`](https://github.com/alekseik1/ifg-py/commit/1c1916671c974708a5dae0039b4c7392b46958fd))

* fix: don&#39;t show plots ([`89b97d7`](https://github.com/alekseik1/ifg-py/commit/89b97d75f693d766e9e96406725579ed42c9fd76))

* fix: plot mu/T instead of mu; plot C_S^2 instead of C_S ([`b1171c6`](https://github.com/alekseik1/ifg-py/commit/b1171c6253ca8d556468196565b815a520d9e026))

* fix: incorrect syntax ([`e3d2c33`](https://github.com/alekseik1/ifg-py/commit/e3d2c33e48696ce51afa150bfffffe154ac7d951))

* fix: remove unused import ([`2f77e7e`](https://github.com/alekseik1/ifg-py/commit/2f77e7eeb4476696d7a2f0d7c6183ad7e2660b1e))

### Style

* style(setup.cfg): exclude venv from flake8 ([`d07f4c5`](https://github.com/alekseik1/ifg-py/commit/d07f4c5601d821d763dfabb2351a76170cbafd18))

* style(setup.cfg): semantic release config ([`cf1b028`](https://github.com/alekseik1/ifg-py/commit/cf1b0283696852a7150ae87e08368a6270f24207))

### Test

* test: increase deadline for C_P low-temp test ([`4eaa8aa`](https://github.com/alekseik1/ifg-py/commit/4eaa8aad6a54b538a0e2868a4a75a2cefbba3b4d))

### Unknown

* Merge pull request #20 from alekseik1/fix/setup

build(setup.cfg): upload to PyPi ([`4c33c15`](https://github.com/alekseik1/ifg-py/commit/4c33c159ccb65d437fe3679f78a018325b1b34ce))

* Merge pull request #19 from alekseik1/semantic_versioning

Semantic versioning ([`fe31161`](https://github.com/alekseik1/ifg-py/commit/fe311619361da3a969fadacd8a91ac66ac03c318))

* Merge pull request #18 from alekseik1/github_actions

GitHub actions ([`7e18b02`](https://github.com/alekseik1/ifg-py/commit/7e18b02460e0350e62ed065191a4cc55f5cd57bf))

* CI: tolerate existing test builds ([`acbad60`](https://github.com/alekseik1/ifg-py/commit/acbad603b264076582b04e01127830588f646219))

* CI: build only wheel package ([`00a7501`](https://github.com/alekseik1/ifg-py/commit/00a75010b5fd14eaa7dc990ed7a8c3cb823921a0))

* CI: fix deploy condition ([`72c9a4e`](https://github.com/alekseik1/ifg-py/commit/72c9a4e1d984999a4a4afc14878f06ffed236186))

* CI: deploy to test PyPi ([`129fe8b`](https://github.com/alekseik1/ifg-py/commit/129fe8bb8cb7e63552ab60b416420ee64a476eff))

* CI: shorten names ([`c12753f`](https://github.com/alekseik1/ifg-py/commit/c12753f2b37e5aee8a74a301a3f03eefb0e0d5dd))

* CI: download artifact to dist/ folder for correct upload ([`015e420`](https://github.com/alekseik1/ifg-py/commit/015e420de0c69a327bd5e6b789760dcbb6c287da))

* CI: cache PIP packages ([`d351542`](https://github.com/alekseik1/ifg-py/commit/d35154213405e14470c035ebffaf605e0310616e))

* CI: `build` depends on `test` ([`4fa054b`](https://github.com/alekseik1/ifg-py/commit/4fa054b771c211bb6af397225049a027ec03e016))

* CI: split build and deploy stages ([`cc3cc49`](https://github.com/alekseik1/ifg-py/commit/cc3cc497d00f358111ad525259fe7b5d6d8f01c3))

* CI: run deploy only after tests ([`3fa7c41`](https://github.com/alekseik1/ifg-py/commit/3fa7c41f38b7d9b8db0b2af6b07a5fe6e986f71b))

* CI: run examples ([`9e1ae0a`](https://github.com/alekseik1/ifg-py/commit/9e1ae0ac5594f3ab66b7aedc69032ba305d3fcdb))

* CI: install numpy in advance ([`0aff2ac`](https://github.com/alekseik1/ifg-py/commit/0aff2ac52b93a77e72260e6d04f4552bb3b2efbf))

* CI: fix syntax ([`1c88c4a`](https://github.com/alekseik1/ifg-py/commit/1c88c4a940ab866bbc54bc3bc6deb7a03df92ba2))

* CI: fix `runs-on` ([`fc1e2c9`](https://github.com/alekseik1/ifg-py/commit/fc1e2c9b818cd73c05ae791d9c3e612612c6b8fd))

* CI: mandatory `on` condition ([`c870bcd`](https://github.com/alekseik1/ifg-py/commit/c870bcd6c7d62cf902ce836d6fdc0d7b6540df71))

* CI: remove Travis config ([`f54889b`](https://github.com/alekseik1/ifg-py/commit/f54889bff03732843f539da29988cd1d49c14c71))

* CI: mvp for github actions ([`1cbde3a`](https://github.com/alekseik1/ifg-py/commit/1cbde3a11a785d57c63eb4d1ac423d57b9f08536))

* doc: fix Travis icon URL ([`66a044c`](https://github.com/alekseik1/ifg-py/commit/66a044ca7214da616da94d0551f97618610c0d9c))

* CI: deploy only on tags ([`66fff2c`](https://github.com/alekseik1/ifg-py/commit/66fff2c3235835eb9856b64d8e2decb5ca9550d0))

* Merge pull request #16 from alekseik1/additions

Additions ([`beea682`](https://github.com/alekseik1/ifg-py/commit/beea682bc9dd2a20d3d50b32ee3980a1f4229ae4))

* ref: cleanup ([`ea31c47`](https://github.com/alekseik1/ifg-py/commit/ea31c4733a1a429178238744d13ea0b98e711561))

* ref: remove class Params ([`cbd6fbb`](https://github.com/alekseik1/ifg-py/commit/cbd6fbb371429f8c8ceb5f646e06a01201a3fe18))

* doc: warn about specificity of some properties
build: increase version ([`2fcd1fc`](https://github.com/alekseik1/ifg-py/commit/2fcd1fc46dfc3669dad324b5041e7a8f4af5b77d))

* tests: consider relative volume ([`908b690`](https://github.com/alekseik1/ifg-py/commit/908b690b8723dffc05e3402bdd3c6c2b3705b589))

* Corrected imports in the header ([`0ebb924`](https://github.com/alekseik1/ifg-py/commit/0ebb92466907a467743f659d6c4290631d1e7b03))

* Corrected SI units, added fermion degeneracy and mass, documentation

Added example of usage into __init__py
Added possibility to input spin degenracy and fermion mass relative
to electron mass
Changed SI units for some values (for extensive values such as
energy, entropy). ([`2f5d163`](https://github.com/alekseik1/ifg-py/commit/2f5d1639fe0e2a4d2f4ea7694c8da25bee2e881e))

* Merge pull request #15 from alekseik1/ci/simplify

Ci/simplify ([`192222f`](https://github.com/alekseik1/ifg-py/commit/192222f96f448611b74b6bf8289cc5a9478c7b50))

* Merge pull request #14 from alekseik1/fix/#13

Fix/#13 ([`c7f5325`](https://github.com/alekseik1/ifg-py/commit/c7f5325e31a782a66947d4a8c3381c029ad8a79e))

* CI: fix build path ([`2b8c9dd`](https://github.com/alekseik1/ifg-py/commit/2b8c9dd810a5701e233994af5adb3705849d9ddf))

* CI: use new processors on Travis ([`2bbb2c3`](https://github.com/alekseik1/ifg-py/commit/2bbb2c38f42ac1f41256c0add969c56711035264))

* CI: stop using docker ([`5673557`](https://github.com/alekseik1/ifg-py/commit/56735573dac79aca4437e097b76f63b78aaeb3ef))

* doc: examples ([`2e3bc47`](https://github.com/alekseik1/ifg-py/commit/2e3bc47b27c22640c3d6ef5ef4e7b027c1e96343))

* ref: rename p -&gt; P ([`a8a07e1`](https://github.com/alekseik1/ifg-py/commit/a8a07e1ed499b440439494fcd38d15a56ebcfc51))

* deps: install numpy before fdint ([`7581112`](https://github.com/alekseik1/ifg-py/commit/7581112f1f83a075ad0dab74ce65dd1402e08909))

* Fix/package installation (#12)

build: improve CI config ([`f13b739`](https://github.com/alekseik1/ifg-py/commit/f13b7399e0c438f64d042d8c79a3fc4874382d09))

* Merge branch &#39;master&#39; into fix/package_installation ([`0c5e0e6`](https://github.com/alekseik1/ifg-py/commit/0c5e0e6979d54886e37a1aec4086e9d1b2e09045))

* doc: warn about numpy preliminary installation ([`f749968`](https://github.com/alekseik1/ifg-py/commit/f749968a3d8c68f2fd1774c5d8f82690068276e6))

* bad: remove python 3.5 tests ([`2c60a0c`](https://github.com/alekseik1/ifg-py/commit/2c60a0c8a65a06d0df34eedc00d41edc3c45e5cb))

* doc: incorrect package name on index page ([`46ce1ce`](https://github.com/alekseik1/ifg-py/commit/46ce1cea4b1bda7e09ddb3af1688603e9b8fed89))

* doc: declare temperature and volume limits on the main page ([`fddeadb`](https://github.com/alekseik1/ifg-py/commit/fddeadb6116033d8854c4aee1dd61d103d4ef239))

* doc: fix module name in README ([`7b9b69b`](https://github.com/alekseik1/ifg-py/commit/7b9b69bd7d35ebcd53693d62728d204fa6499be4))

* ref: rename module to `ifg` ([`0cf720f`](https://github.com/alekseik1/ifg-py/commit/0cf720f095f82e297f8a4ab937fb7043ed961630))

* ref: rename `ifg` to `calculator` ([`37406e4`](https://github.com/alekseik1/ifg-py/commit/37406e48903ac3a0d6206279229042ec0cbe913c))

* tests: improve tests for volume array ([`fdbedb3`](https://github.com/alekseik1/ifg-py/commit/fdbedb33bd2f086db0a511f5902b7a9923b474a5))

* Merge pull request #8 from alekseik1/ref/pytest

Ref/pytest ([`8d3ef7a`](https://github.com/alekseik1/ifg-py/commit/8d3ef7a9f0431f5dd22e3e9b68304c3c8f80339f))

* CI: don&#39;t install requirements before entering tox ([`a1c98f1`](https://github.com/alekseik1/ifg-py/commit/a1c98f115cd4cd6d2ea8dbf46777867e32c6fdd8))

* cleanup: remove unused tests from unittest library ([`172cdd8`](https://github.com/alekseik1/ifg-py/commit/172cdd872ba4c9d02f5488212a67c58777ed1505))

* tests: add test for left-right limits around threshold ([`5104c34`](https://github.com/alekseik1/ifg-py/commit/5104c34fd525280e2208bd87a9bfb892255a14e8))

* ref: move volume and temperatures strategies to conftest.py
ref: move `set_up` to conftest.py ([`68c3e49`](https://github.com/alekseik1/ifg-py/commit/68c3e492baeae0e93b67bb12473f1d1cd4c1beae))

* tests: (ht) mu, F, C_S, C_T, C_P, C_V, S ([`a3f6489`](https://github.com/alekseik1/ifg-py/commit/a3f6489a304e1f02d4d51242783f51f4c095762a))

* tests: (ht) pressure ([`e4eeb7f`](https://github.com/alekseik1/ifg-py/commit/e4eeb7f983f2a365345588748cc488bb96e407c4))

* tests: add low temperature tests for S, C_V, C_P, C_T, C_S, F ([`d1703ff`](https://github.com/alekseik1/ifg-py/commit/d1703ff3a3f8db2f7d4930bf5bdd91e73eb55101))

* tests: move setUp to context manager ([`697b02c`](https://github.com/alekseik1/ifg-py/commit/697b02cfc21c5b669a9393163c4df9df6d5df24d))

* tests: add tests for low temperature mu and p ([`bb3d34c`](https://github.com/alekseik1/ifg-py/commit/bb3d34c9ecddf2e7fa8da55d573f2b063632b129))

* BAD: run only unit tests for pytest in tox.ini ([`b8904f9`](https://github.com/alekseik1/ifg-py/commit/b8904f9980e6298fb90281a8c4f286aded43edec))

* tests: add tests for converter ([`69d828d`](https://github.com/alekseik1/ifg-py/commit/69d828debbb30d68917d79273b3a20ee32422f1c))

* Merge pull request #5 from alekseik1/dev ([`d03a478`](https://github.com/alekseik1/ifg-py/commit/d03a4783f8c35a8d57fb61ffb7e67788c389da53))

* ref: properties instead of functions. Shorter names ([`eeaf45e`](https://github.com/alekseik1/ifg-py/commit/eeaf45efe271fc6437c5ac109e39ea7ecc3d3f41))

* ref: generic getter for duplicating code ([`c86dde3`](https://github.com/alekseik1/ifg-py/commit/c86dde3d16c4245082d514c8fcc60bc4e72112ef))

* flake: max line length -&gt; 100 ([`00b21d9`](https://github.com/alekseik1/ifg-py/commit/00b21d9b911c1ad738ee332f06ab3b51fc62c2db))

* Merge pull request #4 from alekseik1/feat/tests

Feat/tests ([`456b487`](https://github.com/alekseik1/ifg-py/commit/456b4870d6d64590de5653f3c938216d5afb7d45))

* tests: asymptotics for Cp and Cv ([`3c2eb9c`](https://github.com/alekseik1/ifg-py/commit/3c2eb9cd348149e6d3095feb4f00557dd81505c6))

* tests: fix build for Python==2.7 ([`65810d2`](https://github.com/alekseik1/ifg-py/commit/65810d2815b4733042033c392a85bb9e2b46c936))

* tests: Converter class ([`a0b475a`](https://github.com/alekseik1/ifg-py/commit/a0b475ae47ca3144da2ea8d052522ac08996ee80))

* ref: move `convert_density` out of Converter class ([`5bbec68`](https://github.com/alekseik1/ifg-py/commit/5bbec6821d08fb0f0eb5852f5a3d861824a0f8ce))

* Merge pull request #3 from alekseik1/build/obsolete_sudo

build: remove obsolete `sudo` directive ([`9ff68e7`](https://github.com/alekseik1/ifg-py/commit/9ff68e71488bbd67d4aafb213780fbf4881e8534))

* git: add pre-commit config ([`a0d177c`](https://github.com/alekseik1/ifg-py/commit/a0d177ca1eb76273cd0602e8d61e5f6ec82a3209))

* doc: description and examples for &#39;Class usage&#39; ([`bf5f24a`](https://github.com/alekseik1/ifg-py/commit/bf5f24aef18fadf8232afbf021f73b34f4d845cc))

* doc: &#39;Conversion&#39; section description and examples ([`005d683`](https://github.com/alekseik1/ifg-py/commit/005d683f76208221b38d982a2bc809268be86246))

* doc: remove &#39;functional usage&#39; section since it is very buggy ([`8341d5f`](https://github.com/alekseik1/ifg-py/commit/8341d5ff47198549728c7b6f4843c7a571b66469))

* doc: warn about `from_si` ignorance ([`418dcf4`](https://github.com/alekseik1/ifg-py/commit/418dcf44f63c17c199a2df3167134af1344f4e7e))

* doc: do not duplicate `from_si` param description ([`bc762c1`](https://github.com/alekseik1/ifg-py/commit/bc762c14bd9188e9782ed1641494b5b00c59cf24))

* doc: basic structure ([`ae53e0a`](https://github.com/alekseik1/ifg-py/commit/ae53e0ab87f3dfeaf442ed092f8231ee9c16ddfe))

* ref: move examples to separate folder ([`dd8e069`](https://github.com/alekseik1/ifg-py/commit/dd8e069e6c31992da9c74f81b0f42ce91bcdd68a))

* ref: remove old `main.py` ([`8777e12`](https://github.com/alekseik1/ifg-py/commit/8777e120df1fbf565936fee21b3b51c41b05d39b))

* ref: remove notebooks ([`4687706`](https://github.com/alekseik1/ifg-py/commit/468770609aec8ed4e4e1e41ccb1a425fbb435313))

* ref: rename package ([`8871912`](https://github.com/alekseik1/ifg-py/commit/8871912dd21a284ac1d2dcebaf16e79bc9795c9b))

* ref: add license ([`bcc69ad`](https://github.com/alekseik1/ifg-py/commit/bcc69ad6d78c1f0f348ccca840a451b2c75ab381))

* ref: move source code to the module folder ([`7880928`](https://github.com/alekseik1/ifg-py/commit/78809285b1041100428c685d48bcba3bbeeb8622))

* ref: more comments ([`f8fdf63`](https://github.com/alekseik1/ifg-py/commit/f8fdf63a59affa484cfda1af7dc7c4b2b0d25ca6))

* ref: change signature
fix: add `plot_dir` description to docs ([`3bb9126`](https://github.com/alekseik1/ifg-py/commit/3bb91266323e4b7214c7408dd8c4099684a689a8))

* ref: small comment ([`1aa6189`](https://github.com/alekseik1/ifg-py/commit/1aa618971b299ec7defe45bfd2afca5062704e35))

* fixme: hack for proper asymptotic ([`9a69bdf`](https://github.com/alekseik1/ifg-py/commit/9a69bdf5f8ddc3eb4a55aa5c4d7b0ac74477117a))

* exper: make T_range really high ([`e2f41bb`](https://github.com/alekseik1/ifg-py/commit/e2f41bb1b2604edb6b24f964a093b6c4f9072d19))

* notebook upload ([`7e741b6`](https://github.com/alekseik1/ifg-py/commit/7e741b6ad971e0d2cc9db55815d35ae454cbe19a))

* some notebook changes ([`ad4ddce`](https://github.com/alekseik1/ifg-py/commit/ad4ddce5458081c71e01ca4b9eafd6338deb1ff5))

* update .gitignore ([`9b1197f`](https://github.com/alekseik1/ifg-py/commit/9b1197f64f73faf329bdf4a3eb6860b72b6ac143))

* add SI version of program ([`a736953`](https://github.com/alekseik1/ifg-py/commit/a736953d3c63e19a67f14c729a4e5c2b6de1329c))

* README ([`e5650d2`](https://github.com/alekseik1/ifg-py/commit/e5650d2d466ebfd1433133e14d270e9143c4bedd))

* hw1 is done! ([`07d770d`](https://github.com/alekseik1/ifg-py/commit/07d770dabbca7e33364cac41020362b00ebaf2c5))

* add .gitignore ([`9966930`](https://github.com/alekseik1/ifg-py/commit/9966930df1aad751cdec613a95aa4c31bcd8467c))
