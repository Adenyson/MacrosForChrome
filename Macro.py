from selenium import webdriver
import time


class Macror:
    def __init__(self):
        self.ContuntoDeDados = ["ProduçãodatasetMenu11","ExpedidossemFaturardatasetMenu13"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def Clicar(self):
        self.driver.get('https://app.powerbi.com/groups/ae9e166d-9632-429f-be7b-1008688a7bda/list/dashboards?noSignUpCheck=1')
        time.sleep(30)
        for x in range(1):
            Dataset = self.driver.find_element_by_xpath("//a[@localize='ContentList_Datasets']")
            Dataset.click()
            time.sleep(20)

        for x in range(2):
            for ContuntoDeDado in self.ContuntoDeDados:
                ContuntoDeDado = self.driver.find_element_by_xpath(f"//button[@aria-describedby='{ContuntoDeDado}']")
                ContuntoDeDado.click()
                if ContuntoDeDado == "ProduçãodatasetMenu11":
                    time.sleep(300)
                else:
                    time.sleep(60)          

        
#link:  https://app.powerbi.com/groups/ae9e166d-9632-429f-be7b-1008688a7bda/list/dashboards?noSignUpCheck=1 
        # Conjunto de dados:      <a _ngcontent-pme-c21="" class="artifactTab mat-tab-link ng-star-inserted" draggable="false" localize="ContentList_Datasets" mat-tab-link="" queryparamshandling="merge" role="tab" routerlink="datasets" routerlinkactive="" aria-selected="false" aria-disabled="false" tabindex="0" href="/groups/ae9e166d-9632-429f-be7b-1008688a7bda/list/datasets?noSignUpCheck=1">Conjuntos de dados</a>

        # Produçao :   <button class="refreshNow pbi-glyph pbi-glyph-refresh" localize-tooltip="RefreshNow" ng-if="::$ctrl.canRefreshNow" ng-click="$ctrl.runAction($ctrl.RefreshNow)" aria-describedby="ProduçãodatasetMenu11" use-tooltip-as-aria-label="" title="Atualizar agora" aria-label="Atualizar agora"></button>

        # Expedidos sem Faturar:    <button class="refreshNow pbi-glyph pbi-glyph-refresh" localize-tooltip="RefreshNow" ng-if="::$ctrl.canRefreshNow" ng-click="$ctrl.runAction($ctrl.RefreshNow)" aria-describedby="ExpedidossemFaturardatasetMenu13" 
bot = Macror()
bot.Clicar()
