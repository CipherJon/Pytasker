const path = require('path');

module.exports = {
    entry: './app/static/js/app.js',
    output: {
        path: path.resolve(__dirname, 'app/static/js'),
        filename: 'bundle.js'
    },
    mode: 'development', // Set the mode to 'development' or 'production'
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
    devServer: {
        contentBase: path.join(__dirname, 'app/templates'),
        compress: true,
        port: 9000
    }
};