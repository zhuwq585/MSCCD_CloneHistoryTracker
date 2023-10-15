const fs = require('fs');
const parser = require('@babel/parser');
const traverse = require('@babel/traverse');
const { default: generate } = require('@babel/generator');
const args = process.argv;

if (args.length >= 3) {

  // const filePath = '/Users/syu/TestRepos/JavaScript/iotagent-json/lib/iotagent-json.js'; // Replace with the path to your JavaScript file
  const filePath = args[2];

  const code = fs.readFileSync(filePath, 'utf8');

  const ast = parser.parse(code, {
    sourceType: 'module',
    plugins: ['jsx'],
  });

  const functions = [];

  traverse.default(ast, {
    FunctionDeclaration(path) {
      functions.push({
        name: path.node.id.name,
        startLine: path.node.loc.start.line,
        endLine: path.node.loc.end.line,
        type: path.node.type,
        generator : path.node.generator,
        async : path.node.async,
        params : path.node.params
      });
    },
    FunctionExpression(path) {
      if (path.parent.type === 'VariableDeclarator') {
        functions.push({
          name: path.node.id.name,
          startLine: path.node.loc.start.line,
          endLine: path.node.loc.end.line,
          type: path.node.type,
          generator : path.node.generator,
          async : path.node.async,
          params : path.node.params
        });
      }
    },
  });

  // console.log('List of functions:');
  functions.forEach((fn) => {
    // console.log(`Name: ${fn.name}`);
    // console.log(`Start Line: ${fn.startLine}`);
    // console.log(`End Line: ${fn.endLine}`);
    // console.log('-----');
    console.log(JSON.stringify(fn))
  });

}
// You can also output this data to a JSON file or use it as needed.
