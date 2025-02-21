const path = require('path');

module.exports = {
    entry: './src/index.js', // Ensure this path is correct
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'dist'),
    },
    // Other configurations...
}; 