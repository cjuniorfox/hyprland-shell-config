{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenvNoCC.mkDerivation {
  pname = "hyprland-shell-config";
  version = "1.0.37";

  src = ./.;
  dontBuild = true;

  installPhase = ''
    runHook preInstall

    install -d "$out/etc/skel/.config"/{hypr,waybar,rofi,environment.d,systemd/user}

    cp -r hypr/. "$out/etc/skel/.config/hypr/"
    cp -r waybar/. "$out/etc/skel/.config/waybar/"
    cp -r rofi/. "$out/etc/skel/.config/rofi/"
    cp -r environment.d/. "$out/etc/skel/.config/environment.d/"
    cp -r systemd/user/. "$out/etc/skel/.config/systemd/user/"

    touch "$out/etc/skel/.config/hypr/monitors.conf"

    runHook postInstall
  '';

  meta = with pkgs.lib; {
    description = "Hyprland shell configuration files";
    homepage = "https://pagure.io/hyprland-shell-config";
    license = licenses.gpl3Only;
    platforms = platforms.linux;
  };
}
