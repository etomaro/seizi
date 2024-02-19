function createData(
    id,
    prefecture,
    name,
    twitter_id,
    follower,
    follow,
    district
) {
    return {
        id,
        prefecture,
        name,
        twitter_id,
        follower,
        follow,
        district,
    };
}

export const datas = [
    createData(1, "北海道", "岩本剛人", "@iwamoto_tsuyo", 1726, 377, "自民"),
    createData(2, "北海道", "勝部 賢志", "@katsubekenji", 1368, 99, "立憲"),
    createData(
        3,
        "北海道",
        "高橋 はるみ",
        "@harumi_takahasi",
        1873,
        585,
        "自民"
    ),
    createData(
        4,
        "北海道",
        "徳永 エリ(鈴木 エリ)",
        "@tokunaga_eri",
        4043,
        1165,
        "立憲"
    ),
    createData(5, "北海道", "長谷川 岳", "@gaku_hasegawa", 2181, 126, "自民"),
    createData(6, "北海道", "船橋 利実", "@t_funahashi1020", 1612, 153, "自民"),
    createData(7, "青森県", "滝沢 求", "@takisawamotome", 1581, 8, "自民"),
    createData(8, "青森県", "田名部 匡代", "@masayo_tanabu", 2662, 315, "立憲"),
    createData(9, "岩手県", "横沢 高徳", "@TeamYokosawa", 4486, 565, "立憲"),
    createData(10, "岩手県", "広瀬 めぐみ", "@iwate2megumi", 2570, 702, "自民"),
    createData(
        11,
        "宮城県",
        "石垣 のりこ(小川 のり子)",
        "@norinotes",
        70000,
        409,
        "立憲"
    ),
    createData(12, "宮城県", "櫻井 充", "@DrSakurai", 3300, 1, "自民"),
    createData(13, "秋田県", "寺田 静", "@teratashizuka", 4921, 476, "無所属"),
    createData(14, "秋田県", "石井 浩郎", "@hirooishii6", 1973, 83, "自民"),
    createData(15, "山形県", "芳賀 道也", "@hagamichiya", 2034, 776, "民主"),
    createData(
        16,
        "山形県",
        "舟山 康江",
        "@yasue_funayama0",
        3624,
        327,
        "民主"
    ),
    createData(
        17,
        "福島県",
        "森 まさこ(三好 雅子)",
        "@morimasakosangi",
        52000,
        701,
        "自民"
    ),
    createData(18, "福島県", "星 北斗", "@hoshihokuto_web", 820, 124, "自民"),
    createData(19, "茨城県", "小沼 巧", "@onuchan1221", 2558, 329, "立憲"),
    createData(20, "茨城県", "上月 良祐", "@kozuki_ryosuke", 1726, 377, "自民"),
    createData(21, "茨城県", "加藤 明良", "@katoakiyoshi", 1357, 918, "自民"),
    createData(
        22,
        "茨城県",
        "堂込 麻紀子",
        "@Dougomi_Makiko",
        1080,
        537,
        "無所属"
    ),
];
