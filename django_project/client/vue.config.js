const path = require("path");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const fs = require("fs");

module.exports = {
  // Google Sign-in (Customizing the automatically rendered sign-in button Way)
  // chainWebpack: config => {
  //   config.plugin("html").tap(args => {
  //     args[0].meta = {
  //       "google-signin-client_id": process.env.VUE_APP_GOOGLE_CLIENT_ID
  //     };
  //     return args;
  //   });
  // },
  devServer: {
    https: {
      key: fs.readFileSync(`${__dirname}/src/assets/https/localhost-key.pem`),
      cert: fs.readFileSync(`${__dirname}/src/assets/https/localhost.pem`)
    }
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
