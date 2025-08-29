# Ввод параметров при запуске
param(
    [Parameter(Position=0)]
    [ValidateSet('DHCP','Static','Info')]
    [string]$Mode,
    
    [Parameter(Position=1)]
    [string]$Interface,
    [Parameter(Position=2)]
    [string]$Address,
    [Parameter(Position=3)]
    [string]$Mask,
    [Parameter(Position=4)]
    [string]$Gateway,
    [Parameter(Position=5)]
    [string]$DNS,
    
    [switch]$Help,
    [switch]$List
)

# Отображение меню
function Show-Menu {
    Write-Host "=== Network Configurator ==="
    Write-Host "1. Configure DHCP"
    Write-Host "2. Configure Static IP"
    Write-Host "3. Show Interface Info"
    Write-Host "4. List Interfaces"
    Write-Host "5. Help"
    Write-Host "6. Exit"
}

# Отображение справки
function Show-Help {
    Write-Host "Usage:"
    Write-Host "  DHCP config:     .\script7.ps1 -Mode DHCP -Interface 'Ethernet'"
    Write-Host "  Static IP:       .\script7.ps1 -Mode Static 'Ethernet' 192.168.1.100 24 192.168.1.1 8.8.8.8"
    Write-Host "  Interface info:  .\script7.ps1 -Mode Info -Interface 'Ethernet'"
    Write-Host "  List interfaces: .\script7.ps1 -List"
    Write-Host "  Help:            .\script7.ps1 -Help"
}

# Флаг List - список всех интерфейсов
if ($List) {
    Get-NetAdapter
    exit
}
# Флаг Help - справка
if ($Help) { 
    Show-Help 
    exit
}

# Интерактивный режим, если режим работы не введён
if (-not $Mode) {
    Show-Menu
    $choice = Read-Host "Select action"
    
    switch ($choice) {
        '1' { $Mode = 'DHCP' }
        '2' { $Mode = 'Static' }
        '3' { $Mode = 'Info' }
        '4' { $List = $true }
        '5' { $Help = $true }
        '6' { exit }
    }
}

# Пункт меню List - список всех интерфейсов
if ($List) {
    Get-NetAdapter
    exit
}
# Пункт меню Help - справка
if ($Help) { 
    Show-Help 
    exit
}

# Проверка на ввод: имя интерфейса
if (-not $Interface) {
    $Interface = Read-Host "Enter interface name"
}

# Проверка на существование интерфейса
try {
    $Adapter = Get-NetAdapter -Name $Interface -ErrorAction Stop
}
catch {
    Write-Host "Error: Interface $Interface not found!"
    exit
}

# Выбор режима работы
switch ($Mode.ToUpper()) {
    'DHCP' {
        Set-NetIPInterface -InterfaceAlias $Interface -Dhcp Enabled
        Set-DnsClientServerAddress -InterfaceAlias $Interface -ResetServerAddresses

        Write-Host "DHCP configuration applied" -ForegroundColor Green
    }
    
    'STATIC' {
        if (-not $Address) { $Address = Read-Host "Enter IP address" }
        if (-not $Mask) { $Mask = Read-Host "Enter mask (e.g., 24)" }
        if (-not $Gateway) { $Gateway = Read-Host "Enter gateway" }
        if (-not $DNS) { $DNS = Read-Host "Enter DNS server" }
    
        Remove-NetIPAddress -InterfaceAlias $Interface -Confirm:$false
        New-NetIPAddress -InterfaceAlias $Interface -IPAddress $Address -PrefixLength $Mask -DefaultGateway $Gateway | Out-Null
        Set-DnsClientServerAddress -InterfaceAlias $Interface -ServerAddresses $DNS

        Write-Host "Static configuration applied" -ForegroundColor Green
    }
    
    'INFO' {
        # Получение инфы по адаптеру
        $AdapterInfo = Get-NetAdapter -Name $Interface | Select-Object *
        # Статус подключния
        $status = switch ($AdapterInfo.Status) {
            'Up' { 'Connected'; break }
            'Disconnected' { 'Disconnected'; break }
            default { $_ }
        }
        # Дуплекс
        $duplex = switch ($AdapterInfo.MediaDuplexState) {
            '0' { 'Unknown'; break }
            '1' { 'HalfDuplex'; break }
            '2' { 'FullDuplex'; break }
            '3' { 'Auto'; break }
            default { $_ }
        }

        Write-Host "Adapter information"
        Write-Host "Interface Name      =" $AdapterInfo.Name
        Write-Host "MAC Address         =" $AdapterInfo.MacAddress
        Write-Host "Adapter Model       =" $AdapterInfo.InterfaceDescription
        Write-Host "Status              =" $status
        # Write-Host "Physical Connection =" $AdapterInfo.MediaConnectionState
        Write-Host "Speed               =" $AdapterInfo.LinkSpeed
        Write-Host "Duplex Mode         =" $duplex
    }
}