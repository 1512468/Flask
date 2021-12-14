# General
- run app node ```node script.js```
- run app with mode debug ```node --inspect script.js``` 
- run app with mode debug, other port ```node inspect --port=xxxx script.js``` 
# Node js with command line
- input dat from console with inquirer package
# Where does npm install the packages?
- a local install
- a global install
  - By default, when you type an npm install command, like ```npm install lodash```
  - A global installation is performed using the -g flag ```npm install -g lodash```
# Something note about package.json
```sh
there are lots of things going on here:
    - version indicates the current version
    - name sets the application/package name
    - description is a brief description of the app/package
    - main sets the entry point for the application
    - private if set to true prevents the app/package to be accidentally published on npm
    - scripts defines a set of node scripts you can run
    - dependencies sets a list of npm packages installed as dependencies
    - devDependencies sets a list of npm packages installed as development dependencies
    - engines sets which versions of Node.js this package/app works on
    - browserslist is used to tell which browsers (and their versions) you want to support
```
# Install package with version
You can install an old version of an npm package using the @ syntax:
```sh
Ex: 
npm install express@1.1.2
npm install -g webpack@4.16.4

```
