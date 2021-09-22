chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === "complete" && /^http/.test(tab.url)) {
      chrome.scripting.insertCSS({
          target: { tabId: tabId},
          
      })
          .then(() => {
              chrome.scripting.executeScript({
                  target: { tabId: tabId},
                  files: ["foreground.js"]
              })
                  .then(() => {
                      console.log("FOREGROUND INJECTED")
                  })
      })
          .catch(err => console.log(err))
  }
})