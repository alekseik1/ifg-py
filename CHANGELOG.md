# Changelog

<!--next-version-placeholder-->

## v2.1.1 (2021-09-27)
### Fix
* **calculator:** Examples ([`b5a71ab`](https://github.com/alekseik1/ifg-py/commit/b5a71abb78d41cd8fe9a05460481107dcada3a9c))
* Flake errors ([`405eacf`](https://github.com/alekseik1/ifg-py/commit/405eacf3eab85bb5cf3f1be16b1c71e7203b2d19))

### Documentation
* **examples:** Fix examples ([`69edc7a`](https://github.com/alekseik1/ifg-py/commit/69edc7a00c5de3aee0cddc03dcaebe02d2a8d1be))
* **examples:** Add example for theta usage ([`fb8f094`](https://github.com/alekseik1/ifg-py/commit/fb8f094b504470f1fcf5c46a611e9556c5dda393))

## v2.1.0 (2021-08-15)
### Feature
* **calculator:** Support for theta under vectorized volume ([`b94c591`](https://github.com/alekseik1/ifg-py/commit/b94c5912c66f5eb0423f70fc92a4a6a65635771a))
* **converter:** Support array volumes in theta ([`1029f72`](https://github.com/alekseik1/ifg-py/commit/1029f72876d57fea7ce2e94f1e643112ef2da7a8))
* **calculator:** Support for theta input ([`2de80dd`](https://github.com/alekseik1/ifg-py/commit/2de80dda9a7c6d23c8a7594c0bf7fe7aeb1575e5))
* **converter:** Converter from theta to temperatures ([`80531f5`](https://github.com/alekseik1/ifg-py/commit/80531f5dd18f36dc16e618280371cb88a7c747eb))

### Fix
* **calculator:** Match theta mesh dimensions with volume ones ([`94fa7e1`](https://github.com/alekseik1/ifg-py/commit/94fa7e1105b1a9cbc2956cc9587547029f616b71))
* **converter:** Make sure `volume` is not an array ([`5eabaa5`](https://github.com/alekseik1/ifg-py/commit/5eabaa5ab249a5ee1dae820999f3d1e56f4b0914))

## v2.0.0 (2021-08-13)
### Feature
* **calculator:** Support for r_s (WIP) ([`7322936`](https://github.com/alekseik1/ifg-py/commit/73229363713f1603f6821217ef46207567e2c170))
* **calculator:** Builder interface for calculator ([`95e96c6`](https://github.com/alekseik1/ifg-py/commit/95e96c64f733316e576322f63193306ad5c85105))

### Fix
* Use gbar as property ([`94dac3a`](https://github.com/alekseik1/ifg-py/commit/94dac3ae6157cb5faaab11dc5a727010efdd6b77))
* **calculator:** Tests for required parameters ([`7a059d7`](https://github.com/alekseik1/ifg-py/commit/7a059d73d3281b305abf0e9b99e9045c00471dbd))
* **examples:** Correct calculator creation ([`723fdf0`](https://github.com/alekseik1/ifg-py/commit/723fdf0272e6e800e08d264bf3358482a691ef47))

### Breaking
* breaks previous input interface  ([`95e96c6`](https://github.com/alekseik1/ifg-py/commit/95e96c64f733316e576322f63193306ad5c85105))

### Documentation
* **calculator:** Comment with r_s formula ([`80ef695`](https://github.com/alekseik1/ifg-py/commit/80ef695f025dd08d0a0f70fe19d83188f80668ef))
* **calculator:** IfgCalculation class documentation ([`d1271a2`](https://github.com/alekseik1/ifg-py/commit/d1271a27d85da4027ac5ec3108b51f51e955b778))
* **readme:** Correct badges ([`7286fd5`](https://github.com/alekseik1/ifg-py/commit/7286fd54bf58038cc58d577f7a771774339f72b0))
* **readme.md:** Add codecov status ([`ca42075`](https://github.com/alekseik1/ifg-py/commit/ca4207501669e63ae824010007229371213240f7))
* **ci:** Comments for stages ([`8e826a3`](https://github.com/alekseik1/ifg-py/commit/8e826a357208a6921c425b2b132ee4366c34d616))
* Merge pull request #24 from alekseik1/comment ([`c009389`](https://github.com/alekseik1/ifg-py/commit/c00938994daa747a80f2a85d135a5621f6758558))

## v1.2.0 (2021-01-07)
### Feature
* Correct get_all_properties ([`2c65491`](https://github.com/alekseik1/ifg-py/commit/2c6549118dc4c30536764af527e6eb3bef058e4e))

### Fix
* Python2.7 crash on `exist_ok` ([`44fbde5`](https://github.com/alekseik1/ifg-py/commit/44fbde5601c5d58657d42081dc227b2ed4dd8bf0))

### Documentation
* **README.md:** Add badge for tests ([`e22209f`](https://github.com/alekseik1/ifg-py/commit/e22209ff729a423d54e5d6ca975b792699c0e6aa))
* Add GitHub Actions build status ([`06dea65`](https://github.com/alekseik1/ifg-py/commit/06dea6551abe26c3be1decd6dce5e9aa8d098e56))

## v1.1.0 (2021-01-07)
### Feature
* Add energy to calculator ([`8cf1e7a`](https://github.com/alekseik1/ifg-py/commit/8cf1e7a4f9d7bc16121d656ad1e71863199905a0))
* Add plots examples ([`c5d2839`](https://github.com/alekseik1/ifg-py/commit/c5d2839995f2489902bfb6ceb075c8472c28218c))
* Get rid of pandas dependency ([`669b1a8`](https://github.com/alekseik1/ifg-py/commit/669b1a8da5e21db1a43f45c67c7f154cd22c2f6f))
* Declare support py>=2.7 ([`ce3be6b`](https://github.com/alekseik1/ifg-py/commit/ce3be6bfecbff77a80be121fe5e3535952a64e5a))
* `tox` framework ([`4d9b2a5`](https://github.com/alekseik1/ifg-py/commit/4d9b2a57f16558674a81851e5c95a21cac3133e4))
* Flake8 linter ([`9b4fd60`](https://github.com/alekseik1/ifg-py/commit/9b4fd60491e88d7fe42b1be4aacd8b6d2d5921a5))
* Class for all calculations ([`1477444`](https://github.com/alekseik1/ifg-py/commit/1477444bcd8e4a89d0cad1f0b65f73188def8a12))
* `get_all_properties` with dumping to csv file ([`6872a53`](https://github.com/alekseik1/ifg-py/commit/6872a53e87e55634ea1a9f0fd3952397fa2d5e5a))
* Save to csv file; ([`7bfa530`](https://github.com/alekseik1/ifg-py/commit/7bfa5301161391efc421cdda7c684b5a03c2709c))
* Ndarray in `get_sound_speed_entropy` ([`dd206f8`](https://github.com/alekseik1/ifg-py/commit/dd206f8bed103333b9ef9e6a9410c2ca03108ef6))
* Ndarray in `get_sound_speed_temperature` ([`2c46447`](https://github.com/alekseik1/ifg-py/commit/2c464475db64ccc1b0c0f53c8273f8e442153e9d))
* Ndarray in `get_heat_capacity_pressure` ([`5876160`](https://github.com/alekseik1/ifg-py/commit/58761608aaceadf8dbf78adc6e6f8a173ee4318c))
* Ndarray in `get_heat_capacity_volume` ([`51ed0d8`](https://github.com/alekseik1/ifg-py/commit/51ed0d85ada56578dd436998fe9c4baf59a55475))
* Ndarray in `get_entropy` ([`e44badc`](https://github.com/alekseik1/ifg-py/commit/e44badcf6b44392e3e404a3e783e25c1152881c5))
* Ndarray in `get_pressure` ([`7c0585c`](https://github.com/alekseik1/ifg-py/commit/7c0585c509a1054133fdab9101ee5c0423bd3e06))
* Ndarray in `get_F_potential` ([`9b5f9d0`](https://github.com/alekseik1/ifg-py/commit/9b5f9d08b38017626d57912d61d6eea027ec7fdb))
* Ndarray in `get_chemical_potential` ([`d918b46`](https://github.com/alekseik1/ifg-py/commit/d918b46548178e78cd23322f8d35fc01cb7c97be))
* Accept *args and **kwargs (just ignore them) ([`091ae08`](https://github.com/alekseik1/ifg-py/commit/091ae085d78dc42dcf84852ad81ab30e2b52ae96))
* Plot mu from T ([`296b8c4`](https://github.com/alekseik1/ifg-py/commit/296b8c40095b123c1e4220b2581f887d3ed1c869))
* Prettify graph visualizer ([`9a5388b`](https://github.com/alekseik1/ifg-py/commit/9a5388b2d3e1b46a7a5108a395aa51cd87dbf65b))
* Add grid to plots ([`2d8e880`](https://github.com/alekseik1/ifg-py/commit/2d8e880f48d953f4ac42bf7e7ed773d8516217c2))
* Example ([`2c1e161`](https://github.com/alekseik1/ifg-py/commit/2c1e161eedb32dd1a48df69352c3bd8c5430534a))
* Converter from density to specific volume in SI ([`8492a3c`](https://github.com/alekseik1/ifg-py/commit/8492a3cd3b6f17bb16f733d332ed67db71d48c10))
* Entropy, heat capacity and sound speed convert ([`1a85503`](https://github.com/alekseik1/ifg-py/commit/1a85503567e91e25ec0532a78ab8f5912ad137de))
* Convert for volume and pressure ([`e0a24f3`](https://github.com/alekseik1/ifg-py/commit/e0a24f31d4058066968baad4d569fec87d4dc8e8))
* Units converter. Energy and temperature only ([`660ae0e`](https://github.com/alekseik1/ifg-py/commit/660ae0ee06eb0091d73cd90c6a7619a867642caa))
* Calculator for atomic units ([`54c946b`](https://github.com/alekseik1/ifg-py/commit/54c946bafb18021a6a7055665ea8e6a7f57dc8bd))

### Fix
* **setup.cfg:** Syntax quotes ([`d6b45bf`](https://github.com/alekseik1/ifg-py/commit/d6b45bf90f44d3acaea7d706b8db0ce3db2833d6))
* Increase version ([`da8920f`](https://github.com/alekseik1/ifg-py/commit/da8920fa0a9f966b3ee92a179092f4087f6d7bb1))
* P -> P in `get_all_properties` ([`a420a50`](https://github.com/alekseik1/ifg-py/commit/a420a50160b02753db1491ec27c14ed7302115e5))
* Duplicate classifiers ([`aafbeef`](https://github.com/alekseik1/ifg-py/commit/aafbeef927ad22a15ad9eab37432ccb6941d2525))
* Better threshold value for low-temperature limits ([`d406b9a`](https://github.com/alekseik1/ifg-py/commit/d406b9a337aeb1218704895d82edbb6cd0396c4d))
* Hypothesis warnings ([`5f96a7d`](https://github.com/alekseik1/ifg-py/commit/5f96a7dc0011565cde53b43981ef8c5f95659231))
* Syntax for py=2.7 in tests ([`c2a16b2`](https://github.com/alekseik1/ifg-py/commit/c2a16b2a763cdd60d74ecb9b8cd32a973d98f851))
* Precision problem on low temperatures ([`9e2b83d`](https://github.com/alekseik1/ifg-py/commit/9e2b83d7534f62b880d91cd66a0900e8cb6b2986))
* Mistype in low temp test for C_S ([`887a800`](https://github.com/alekseik1/ifg-py/commit/887a80007a8dabb95073fddb50ff58f391075f17))
* Change numpy assert functions to `assert_allclose` since they are more stable ([`47e3939`](https://github.com/alekseik1/ifg-py/commit/47e3939289494a8085d39343ecd3905034301fa8))
* Get rid of hypothesis since it is broken for py2.7 ([`b2d54de`](https://github.com/alekseik1/ifg-py/commit/b2d54dedcaa51fb58d0846366325463591d40671))
* True division for py<3 ([`07049b9`](https://github.com/alekseik1/ifg-py/commit/07049b99e93fca042d5f1e1801750e425758b216))
* Less RAM consumption ([`d18dd8d`](https://github.com/alekseik1/ifg-py/commit/d18dd8da9b0b0d554207379742d72fc5d540c012))
* Python2.7 compatibility ([`dc41ab9`](https://github.com/alekseik1/ifg-py/commit/dc41ab913dadfa94493f0ec4f243bbd81301c42e))
* Incorrect converter ([`a1bbd76`](https://github.com/alekseik1/ifg-py/commit/a1bbd76aee29a899a8c51dab130fe658ca5e83dc))
* Cast to np.array ([`9b6c526`](https://github.com/alekseik1/ifg-py/commit/9b6c5268e49fc32b390ffd4551a16ec4ede174dd))
* Fix incorrect power in fdk (float division on python2.*) ([`d7b5194`](https://github.com/alekseik1/ifg-py/commit/d7b519450aeb80e80d4da9b69c7a9dc7a64c0a33))
* Type annotation for python2.7 ([`0bf065f`](https://github.com/alekseik1/ifg-py/commit/0bf065fb1a6eee06da68328587b51dfa371f83cb))
* Typo in convert variable ([`64201aa`](https://github.com/alekseik1/ifg-py/commit/64201aa212dfcd05ace4dd8b6842fb6b17a486fd))
* Support for py>=3.5 ([`26336ee`](https://github.com/alekseik1/ifg-py/commit/26336ee9b62ae0129d2f2e98c5f521190f5d18b2))
* Remove saving data in examples.py ([`58788f3`](https://github.com/alekseik1/ifg-py/commit/58788f3db3dddfda75f700f036dc8215de11800e))
* Flake8 errors ([`f9ff175`](https://github.com/alekseik1/ifg-py/commit/f9ff175a89f5328c43a2c9eeac81926f8b449740))
* Early import crash in both `setup.py` and `conf.py` ([`b5ac91f`](https://github.com/alekseik1/ifg-py/commit/b5ac91f43dad2ac4c6e45e2525ce76515f8ae2b9))
* `setup` script crash because of early imports ([`d58a8bc`](https://github.com/alekseik1/ifg-py/commit/d58a8bc89fcad0c3953ed0d7aed630f9b3bf8cd9))
* `setup_requires` ([`3ce66ab`](https://github.com/alekseik1/ifg-py/commit/3ce66abc93e4ade36bc3c9d7142540c0b282865c))
* Remove redundant dependencies ([`89ae6f2`](https://github.com/alekseik1/ifg-py/commit/89ae6f21808d3077f6dd8a6bd0387e11cee4ff0e))
* Install dependencies ([`6338e91`](https://github.com/alekseik1/ifg-py/commit/6338e91e0d0f36745a0fa3002014b600274a03e0))
* Mark as for Python>=3.6 ([`f4b4c9b`](https://github.com/alekseik1/ifg-py/commit/f4b4c9bb9eb14cb3bffd09c97c33217d304cafaa))
* Broken examples ([`273aa89`](https://github.com/alekseik1/ifg-py/commit/273aa893560d35b6cd7dea3b26e4d15f55628531))
* `get_metal_specific_volume` returns values in SI ([`6091c63`](https://github.com/alekseik1/ifg-py/commit/6091c63edd735557de84f4a11d41ba5ca18b9fbf))
* Missing documentation for functions in `units_converter.py` ([`e8bf0c1`](https://github.com/alekseik1/ifg-py/commit/e8bf0c1e515029282aaff6e63e4e1597fe298788))
* Pass *args and **kwargs to _fdk ([`7ab53d5`](https://github.com/alekseik1/ifg-py/commit/7ab53d597c6324faf34a44d38c85d4e90afef9b6))
* Warn about one parameter as vector problem ([`a2dc37f`](https://github.com/alekseik1/ifg-py/commit/a2dc37f8e2dcecbe15c1f7df474bbd770176a8c2))
* Specify package version in `__init__.py` ([`a78b82f`](https://github.com/alekseik1/ifg-py/commit/a78b82f6370544fc3c72d7ec249c1fae0d385be7))
* Conflict of `master_doc` on local machine and RTD ([`ec53a35`](https://github.com/alekseik1/ifg-py/commit/ec53a352762476efa85eef610ad3b3c54844ce9b))
* Explicitly import functions ([`1c19166`](https://github.com/alekseik1/ifg-py/commit/1c1916671c974708a5dae0039b4c7392b46958fd))
* Don't show plots ([`89b97d7`](https://github.com/alekseik1/ifg-py/commit/89b97d75f693d766e9e96406725579ed42c9fd76))
* Plot mu/T instead of mu; plot C_S^2 instead of C_S ([`b1171c6`](https://github.com/alekseik1/ifg-py/commit/b1171c6253ca8d556468196565b815a520d9e026))
* Incorrect syntax ([`e3d2c33`](https://github.com/alekseik1/ifg-py/commit/e3d2c33e48696ce51afa150bfffffe154ac7d951))
* Remove unused import ([`2f77e7e`](https://github.com/alekseik1/ifg-py/commit/2f77e7eeb4476696d7a2f0d7c6183ad7e2660b1e))

### Documentation
* Icon for CI status ([`f2b9e1d`](https://github.com/alekseik1/ifg-py/commit/f2b9e1df974353333244f739c4a3d67bb47f65fc))
* Fix sphinx warnings ([`b9b4250`](https://github.com/alekseik1/ifg-py/commit/b9b42500d479dc3699e6e3b2addb2b84abbfea52))
* Add missing empty line ([`06a475a`](https://github.com/alekseik1/ifg-py/commit/06a475ad9a9c51a77ffa4803eb574dce4ff721d6))
* Basic readme ([`b3b0914`](https://github.com/alekseik1/ifg-py/commit/b3b0914a0148f6f1027fc67e7c51f77756afef08))
* Add sphinx files ([`e9938db`](https://github.com/alekseik1/ifg-py/commit/e9938dbf229e60db6e09fe38e13d3b3c5a81f094))
* Documentation for `units_converter` ([`515f389`](https://github.com/alekseik1/ifg-py/commit/515f389f60298b4703af687d9dab91b916e849ae))
