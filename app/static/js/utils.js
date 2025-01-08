function convertToBanglaNumbers(englishNumber) {
  const banglaDigits = {
    0: "০",
    1: "১",
    2: "২",
    3: "৩",
    4: "৪",
    5: "৫",
    6: "৬",
    7: "৭",
    8: "৮",
    9: "৯",
  };

  return englishNumber
    .toString()
    .split("")
    .map((char) => banglaDigits[char] || char)
    .join("");
}

const banglaDict = {
  chittagong: "চট্টগ্রাম",
  dhaka: "ঢাকা",
  rajshahi: "রাজশাহী",
  khulna: "খুলনা",
  sylhet: "সিলেট",
  barisal: "বরিশাল",
  rangpur: "রংপুর",
  mymensingh: "ময়মনসিংহ",
};

function translateWordToBangla(word) {
  return banglaDict[word.toLowerCase()] || word;
}
