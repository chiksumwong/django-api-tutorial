const path = require("path");
const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = {
  chainWebpack: config => {
    config.plugin("html").tap(args => {
      args[0].meta = {
        "google-signin-client_id": process.env.GOOGLE_CLIENT_ID
      };
      return args;
    });
  },
  // devServer: {
  //   host: "127.0.0.1",
  //   port: 4000,
  //   https: false,
  //   hotOnly: false,
  //   proxy: null
  // },
  /* package all css js file to static file */
  assetsDir: "static",
  /* to copy public/favicon.ico to dist/static */
  configureWebpack: {
    plugins: [
      new CopyWebpackPlugin([
        {
          from: path.join(__dirname, "/public"),
          to: path.join(__dirname, "/dist/static"),
          toType: "dir",
          ignore: ["index.html"]
        }
      ])
    ]
  }
};
